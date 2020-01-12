# -*- coding: utf-8 -*-

'''
Задание 27.1

Создать класс CiscoSSH, который наследует класс BaseSSH из файла base_connect_class.py.

Создать метод __init__ в классе CiscoSSH таким образом, чтобы после подключения по SSH выполнялся переход в режим enable.

Для этого в методе __init__ должен сначала вызываться метод __init__ класса BaseSSH, а затем выполняться переход в режим enable.

In [2]: from task_27_1 import CiscoSSH

In [3]: r1 = CiscoSSH(**device_params)

In [4]: r1.send_show_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

'''
from base_connect_class import BaseSSH
from getpass import getpass


class CiscoSSH(BaseSSH):
    def __init__(self, **dev_par):
        if not dev_par.get('username', None):
            dev_par['username'] = input('Введите имя пользователя: ')
        if not dev_par.get('password', None):
            dev_par['password'] = input('Введите пароль: ')
        if not dev_par.get('secret', None):
            dev_par['secret'] = input('Введите пароль для режима enable: ')
        super().__init__(**dev_par)
        self.ssh.enable()


# don't run on import
if __name__ == "__main__":
    device_params = {
        'device_type': 'cisco_ios',
        'ip': '10.111.111.11',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco'
    }
    r1 = CiscoSSH(**device_params)
    print(r1.send_show_command('sh ip int br'))
