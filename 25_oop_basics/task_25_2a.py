# -*- coding: utf-8 -*-

'''
Задание 25.2a

Скопировать класс CiscoTelnet из задания 25.2 и изменить метод send_show_command добавив два параметра:

* parse - контролирует то, будет возвращаться обычный вывод команды или список словарей, полученные после обработки
с помощью TextFSM. При parse=True должен возвращаться список словарей, а parse=False обычный вывод
* templates - путь к каталогу с шаблонами



Пример создания экземпляра класса:

In [1]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [2]: from task_25_2a import CiscoTelnet

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_show_command:
In [4]: r1.send_show_command('sh ip int br', parse=False)
Out[4]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nLoopback0                  10.1.1.1        YES NVRAM  up                    up      \r\nLoopback55                 5.5.5.5         YES manual up                    up      \r\nR1#'

In [5]: r1.send_show_command('sh ip int br', parse=True)
Out[5]:
[{'intf': 'Ethernet0/0',
  'address': '192.168.100.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/1',
  'address': '192.168.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/2',
  'address': '190.16.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3',
  'address': '192.168.130.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.100',
  'address': '10.100.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.200',
  'address': '10.200.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.300',
  'address': '10.30.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Loopback0',
  'address': '10.1.1.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Loopback55',
  'address': '5.5.5.5',
  'status': 'up',
  'protocol': 'up'}]
'''
import telnetlib, time
from textfsm import clitable
from re import findall


class CiscoTelnet:
    def _write_line(self, line):
        line = line.encode('cp866')
        self.t.write(line + b'\n')

    def __init__(self, ip, username, password, secret):
        self.ip = ip
        self.t = telnetlib.Telnet(ip)
        self.t.read_until(b'Username:')
        self._write_line(username)
        self.t.read_until(b'Password:')
        self._write_line(password)
        self._write_line('enable')
        self.t.read_until(b'Password:')
        self._write_line(secret)
        self._write_line('terminal length 0')

    def send_show_command(self, sh_command, parse, templates='templates'):
        self._write_line(sh_command)
        time.sleep(1)
        out = self.t.expect([b'[>#]'])[2].decode('cp866')
        if parse:
            cli = clitable.CliTable('index', templates)
            attributes = {'Command': sh_command, 'Vendor': 'Cisco'}
            cli.ParseCmd(out, attributes)
            header = list(cli.header)
            return [dict(zip(header, list(res))) for res in cli]
        else:
            return out

    def send_config_commands(self, commands, strict=None):
        #if isinstance(commands, str): commands = [commands]
        if type(commands) == str: commands = [commands]
        errors = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']
        regex = (r'\(config\)#(.+)\n(?:.*\n)*?% (.+)\n')
        self._write_line('conf t')
        time.sleep(0.3)
        for command in commands:
            self._write_line(command)
            time.sleep(1)
        self._write_line('end')
        time.sleep(0.3)
        result = self.t.read_very_eager().decode('cp866')
        if strict:
            if any(eror in result for eror in errors):
                raise ValueError
        else:
            finds = findall(regex, result)
            if finds:
                for find in finds:
                    print(f'При выполнении команды {find[0].rstrip()} на устройстве {self.ip} возникла ошибка -> {find[1].rstrip()}')
        return result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t.close()

# don't run on import
if __name__ == "__main__":
    r1_params = {'ip': '10.111.111.11',
                 'username': 'admin',
                 'password': 'cisco',
                 'secret': 'cisco'}
    r1 = CiscoTelnet(**r1_params)
    r1.send_show_command('sh ip int br', parse=False)
    r1.send_show_command('sh ip int br', parse=True)

