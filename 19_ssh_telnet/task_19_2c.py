# -*- coding: utf-8 -*-
'''
Задание 19.2c

Скопировать функцию send_config_commands из задания 19.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

'''
from pprint import pprint
import netmiko
from yaml import safe_load
from re import findall


def send_config_commands(device_dict, command_list, verbose=True):
    errors = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']
    good = {}
    bad ={}
    regex = (r'%.+?\n')
    try:
        if verbose: print('Подключаюсь к ' + device_dict['ip'] + '...')
        with netmiko.ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            for command in command_list:
                result = ssh.send_config_set(command)
                if any(eror in result for eror in errors):
                    bad[command] = result
                    print(f'Команда {command} выполнилась с ошибкой {findall(regex, result)[0].rstrip()} на устройстве ' + device_dict['ip'])
                    if input('Продолжать выполнять команды? [y]/n: ') in ('n', 'N'):
                        break
                else:
                    good[command] = result
        return good, bad
    except (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException) as err:
        return err

#don't run on import
if __name__ == '__main__':
    commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
    correct_commands = ['logging buffered 20010', 'ip http server']
    commands = commands_with_errors + correct_commands
    yaml_of_devices = 'devices.yaml'
    with open(yaml_of_devices) as f:
        templ = safe_load(f)
    for device in templ:
        pprint(send_config_commands(device, commands), width=120)

