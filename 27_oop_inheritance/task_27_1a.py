# -*- coding: utf-8 -*-

'''
Задание 27.1a

Дополнить класс CiscoSSH из задания 27.1.

Перед подключением по SSH необходимо проверить если ли в словаре
с параметрами подключения такие параметры: username, password, secret.
Если нет, запросить их у пользователя, а затем выполнять подключение.

In [1]: from task_27_1a import CiscoSSH

In [2]: device_params = {
   ...:         'device_type': 'cisco_ios',
   ...:         'ip': '192.168.100.1',
   ...: }

In [3]: r1 = CiscoSSH(**device_params)
Введите имя пользователя: cisco
Введите пароль:
Введите пароль для режима enable:

In [4]: r1.send_show_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

'''
from task_27_1 import CiscoSSH
from pprint import pprint
import getpass

#don't run on import
if __name__ == "__main__":
    device_params = {
        'device_type': 'cisco_ios',
        'ip': '10.111.11.2'
    }
    r1 = CiscoSSH(**device_params)
    pprint(r1.send_show_command('sh ip int br'), width=120)