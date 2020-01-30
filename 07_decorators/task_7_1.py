# -*- coding: utf-8 -*-
"""
Задание 7.1

Создать декоратор timecode, который засекает время выполнения декорируемой функции
и выводит время на стандартный поток вывода. Декоратор должен работать с любой функцией.

Проверить работу декоратора на функции send_show_command.

Пример вывода:

In [3]: @timecode
   ...: def send_show_command(params, command):
   ...:     with ConnectHandler(**params) as ssh:
   ...:         ssh.enable()
   ...:         result = ssh.send_command(command)
   ...:     return result
   ...:

In [4]: print(send_show_command(device_params, 'sh clock'))
>>> Функция выполнялась: 0:00:05.527703
*13:02:49.080 UTC Mon Feb 26 2018


Тест берет значения из словаря device_params в этом файле, поэтому если
для заданий используются другие адреса/логины, надо заменить их в словаре.
"""

from netmiko import ConnectHandler
from functools import wraps
from datetime import datetime


def timecode(func):
    @wraps(func)
    def wrapper(*args):
        start_time = datetime.now()
        return_res = func(*args)
        print(f'Функция выполнялась: {datetime.now() - start_time}')
        return return_res
    return wrapper


@timecode
def send_show_command(params, command):
    with ConnectHandler(**params) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


if __name__ == "__main__":
    device_params = {
        'device_type': 'cisco_ios',
        'ip': '10.111.111.11',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco'
    }
    print(send_show_command(device_params, 'sh clock'))
