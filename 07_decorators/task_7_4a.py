# -*- coding: utf-8 -*-
"""
Задание 7.4a

Переделать декоратор retry из задания 7.4: добавить параметр delay,
который контролирует через какое количество секунд будет выполняться повторная попытка.
При каждом повторном запуске результат проверяется:

* если он был истинным, он возвращается
* если нет, функция запускается повторно заданное количество раз

Пример работы декоратора:
In [2]: @retry(times=3, delay=5)
    ..: def send_show_command(device, show_command):
    ..:     print('Подключаюсь к', device['ip'])
    ..:     try:
    ..:         with ConnectHandler(**device) as ssh:
    ..:             ssh.enable()
    ..:             result = ssh.send_command(show_command)
    ..:         return result
    ..:     except (NetMikoAuthenticationException, NetMikoTimeoutException):
    ..:         return None
    ..:

In [3]: send_show_command(device_params, 'sh clock')
Подключаюсь к 192.168.100.1
Out[4]: '*16:35:59.723 UTC Fri Oct 18 2019'

In [5]: device_params['password'] = '123123'

In [6]: send_show_command(device_params, 'sh clock')
Подключаюсь к 192.168.100.1
Повторное подключение через 5 сек
Подключаюсь к 192.168.100.1
Повторное подключение через 5 сек
Подключаюсь к 192.168.100.1
Повторное подключение через 5 сек
Подключаюсь к 192.168.100.1


Тест берет значения из словаря device_params в этом файле, поэтому если
для заданий используются другие адреса/логины, надо заменить их в словаре.
"""
import time
from functools import wraps
from netmiko import (ConnectHandler, NetMikoAuthenticationException,
                     NetMikoTimeoutException)


def retry(times, delay):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            rrr = times
            while rrr >= 0:
                result = func(*args)
                rrr -= 1
                if result:
                    return result
                else:
                    if rrr >= 0:
                        print(f'Повторное подключение через {delay} сек')
                        time.sleep(delay)
        return wrapper
    return decorator


@retry(times=3, delay=1)
def send_show_command(device, show_command):
    print('Подключаюсь к', device['ip'])
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(show_command)
        return result
    except (NetMikoAuthenticationException, NetMikoTimeoutException):
        return None


if __name__ == "__main__":
    device_params = {
        'device_type': 'cisco_ios',
        'ip': '10.111.111.11',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco'
    }
    output = send_show_command(device_params, 'sh clock')

