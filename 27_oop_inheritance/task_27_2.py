# -*- coding: utf-8 -*-

'''
Задание 27.2

Создать класс MyNetmiko, который наследует класс CiscoIosBase из netmiko.

Переписать метод __init__ в классе MyNetmiko таким образом, чтобы после подключения по SSH выполнялся переход в режим enable.

Для этого в методе __init__ должен сначала вызываться метод __init__ класса CiscoIosBase, а затем выполнялся переход в режим enable.

Проверить, что в классе MyNetmiko доступны методы send_command и send_config_set

In [2]: from task_27_2 import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

'''
from netmiko.cisco.cisco_ios import CiscoIosBase


class ErrorInCommand(Exception):
    pass

class MyNetmiko(CiscoIosBase):
    def __init__(self, **dev_par):
        super().__init__(**dev_par)
        self.enable()

    def _check_error_in_command(self, command, command_output):
        errors = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']
        for error in errors:
            if error in command_output:
                raise ErrorInCommand(f'При выполнении команды {command} на устройстве {self.host} возникла ошибка {error}')

    def send_command(self, command_string):
        result = super().send_command(command_string)
        self._check_error_in_command(command_string, result)
        return result

# don't run on import
if __name__ == "__main__":
    device_params = {
        'device_type': 'cisco_ios',
        'ip': '10.111.11.2',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco'
    }
    commands = ['logging buffered 20010', 'ip http server']
    r1 = MyNetmiko(**device_params)
    print(r1.send_command('sh ip int br'))
    print(r1.send_config_set(commands))

