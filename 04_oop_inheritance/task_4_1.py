# -*- coding: utf-8 -*-
'''
Задание 4.1

Создать класс CiscoTelnet, который наследует класс TelnetBase из файла base_telnet_class.py.

Переписать метод __init__ в классе CiscoTelnet таким образом:

* добавить параметры:
 * enable - пароль на режим enable
 * disable_paging - отключает постраничный вывод команд, по умолчанию равен True
* после подключения по Telnet должен выполняться переход в режим enable:
  для этого в методе __init__ должен сначала вызываться метод __init__ класса TelnetBase,
  а затем выполняться переход в режим enable.

Добавить в класс CiscoTelnet метод send_show_command, который отправляет команду
show и возвращает ее вывод в виде строки. Метод ожидает как аргумент одну команду.

Добавить в класс CiscoTelnet метод send_config_commands, который отправляет одну
или несколько команд на оборудование в конфигурационном режиме и возвращает ее
вывод в виде строки. Метод ожидает как аргумент одну команду (строку) или
несколько команд (список).

Пример работы класса:
In [1]: r1 = CiscoTelnet('192.168.100.1', 'cisco', 'cisco', 'cisco')

Метод send_show_command:
In [2]: r1.send_show_command('sh clock')
Out[2]: 'sh clock\r\n*09:39:38.633 UTC Thu Oct 10 2019\r\nR1#'

Метод send_config_commands:
In [3]: r1.send_config_commands('logging 7.7.7.7')
Out[3]: 'conf t\r\nEnter configuration commands, one per line.
End with CNTL/Z.\r\nR1(config)#logging 7.7.7.7\r\nR1(config)#end\r\nR1#'

In [4]: r1.send_config_commands(['interface loop77', 'ip address 107.7.7.7 255.255.255.255'])
Out[4]: 'conf t\r\nEnter configuration commands, one per line.
End with CNTL/Z.\r\nR1(config)#interface loop77\r\nR1(config-if)#ip address 107.7.7.7 255.255.255.255\r\nR1(config-if)#end\r\nR1#'


Тест берет значения из файла devices.yaml, поэтому если
для заданий используются другие адреса/логины, надо заменить их там.
'''
from base_telnet_class import TelnetBase
from time import sleep
from yaml import safe_load
from re import findall


class ErrorInCommand(Exception):
    pass


class CiscoTelnet(TelnetBase):
    def __init__(self, ip, username, password, enable, disable_paging=True):
        super().__init__(ip, username, password)
        self._write_line('enable')
        sleep(1)
        self._telnet.read_very_eager()
        #self._read_until_regex('Password:')
        #self._write_line(enable)
        #sleep(1)
        #self._telnet.read_very_eager()
        if disable_paging:
            self._write_line('terminal length 0')
            sleep(1)
            self._telnet.read_very_eager()

    def send_show_command(self, command):
        self._write_line(command)
        sleep(1)
        result = self._telnet.read_very_eager().decode(self.encoding)
        self._check_error_in_command(command, result)
        return result

    def send_config_commands(self, commands):
        if isinstance(commands, str): commands = [commands]
        self._write_line('conf t')
        sleep(1)
        result = self._telnet.read_very_eager().decode(self.encoding)
        for command in commands:
            self._write_line(command)
            sleep(1)
            res = self._telnet.read_very_eager().decode(self.encoding)
            self._check_error_in_command(command, res)
            result += res
        self._write_line('end')
        sleep(1)
        result += self._telnet.read_very_eager().decode(self.encoding)
        return result

    def _check_error_in_command(self, command, command_output):
        errors = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']
        for error in errors:
            if error in command_output:
                regex = error + '.*?\n'
                raise ErrorInCommand(f'При выполнении команды {command} на устройстве {self.ip} '
                                     f'возникла ошибка {findall(regex, command_output)[0]}')


# don't run on import
if __name__ == "__main__":
    with open('devices.yaml') as src:
        devices = safe_load(src)
    with CiscoTelnet(**devices[0]) as r1:
        print(r1.send_show_command('sh clock'))
        print('*'*45)
        print(r1.send_config_commands('logging 7.7.7.7'))
        print('*'*45)
        print(r1.send_config_commands(['interface loop77', 'ip address 107.7.7.7 255.255.255.255']))

