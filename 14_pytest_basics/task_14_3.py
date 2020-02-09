# -*- coding: utf-8 -*-
"""
Задание 14.3

Написать тест(ы), который проверяет есть ли маршрут 192.168.100.0/24 в таблице
маршрутизации (команда sh ip route) на маршрутизаторах, которые указаны в файле devices.yaml.

Для проверки надо подключиться к каждому маршрутизатору с помощью netmiko
и проверить маршрут командой sh ip route или разновидностью команды sh ip route.

Тест(ы) должен проходить, если маршрут есть.
Тест может быть один или несколько.

Тест(ы) написать в файле задания.
"""
import netmiko, yaml
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_output_command(device):
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command('sh ip route')
    return device['host'], result


def find_route_in_devs():
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(get_output_command, device) for device in devices]
        for future in as_completed(futures):
            result = future.result()
            print('*' * 50)
            print(*result)


if __name__ == "__main__":
    find_route_in_devs()