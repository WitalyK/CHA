# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

'''
import netmiko
from yaml import safe_load


def send_show_command(device_dict, command_line):
    try:
        with netmiko.ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command_line)
        return result
    except netmiko.ssh_exception.NetMikoTimeoutException as err:
        return err

#don't run on import
if __name__ == '__main__':
    command = 'sh ip int br'
    yaml_of_devices = 'devices.yaml'
    with open(yaml_of_devices) as f:
        templ = safe_load(f)
    for device in templ:
        print(send_show_command(device, command))