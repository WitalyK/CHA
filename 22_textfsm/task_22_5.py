# -*- coding: utf-8 -*-
'''
Задание 22.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в параллельных потоках функцию send_and_parse_show_command
из задания 22.4.

В этом задании надо самостоятельно решить:
* какие параметры будут у функции
* что она будет возвращать


Теста для этого задания нет.
'''
from task_22_4 import send_and_parse_show_command
from yaml import safe_load
from concurrent.futures import ThreadPoolExecutor, as_completed
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException


def send_and_parse_command_parallel(devs, command):
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(send_and_parse_show_command, dev, command) for dev in devs]
        t_futures = []
        for future in as_completed(futures):
            try:
                for fu in future.result():
                    t_futures.append(fu)
            except (NetMikoAuthenticationException, NetMikoTimeoutException) as e:
                print(e)
    return t_futures

# don't run on import
if __name__ == "__main__":
    with open("devices.yaml") as src:
        devices = safe_load(src)
    list_dict = send_and_parse_command_parallel(devices, 'sh ip int br')
    for line in list_dict:
        print(line)