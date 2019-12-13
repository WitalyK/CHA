# -*- coding: utf-8 -*-
'''
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
'''
import netmiko
from yaml import safe_load


def send_show_command(device_dict, command_line):
    try:
        with netmiko.ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command_line)
        return result
    except (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException) as err:
        return err

#don't run on import
if __name__ == '__main__':
    command = 'sh ip int br'
    yaml_of_devices = 'devices.yaml'
    with open(yaml_of_devices) as f:
        templ = safe_load(f)
    for device in templ:
        print(send_show_command(device, command))
