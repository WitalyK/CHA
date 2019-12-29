# -*- coding: utf-8 -*-
'''
Задание 22.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.
'''
import netmiko
from yaml import safe_load


def send_and_parse_show_command(device_dict, command, templates_path='ntc-templates/templates/', index="index"):
    with netmiko.ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        host = ssh.find_prompt()[:-1]
        res = ssh.send_command(command, use_textfsm=True)
        for r in res:
            r.update({'host': host})
    return res

# don't run on import
if __name__ == "__main__":
    with open("devices.yaml") as src:
        devices = safe_load(src)
    list_dict = send_and_parse_show_command(devices[0], 'sh ip int br', 'ntc-templates/templates/')
    for line in list_dict:
        print(line)