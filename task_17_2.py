# -*- coding: utf-8 -*-
'''
Задание 17.2
Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.
Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.
Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors
Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0
Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}
Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.
Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re


def parse_sh_cdp_neighbors(show_cdp_neighbors_command):
    key = show_cdp_neighbors_command.split('>')[0]
    regex = r'(\w+) +(\w+ \d+/\d+).+ (\w+ \d+/\d+)'
    result = re.finditer(regex, show_cdp_neighbors_command)
    d = {}
    d[key] = {}
    for match in result:
        d[key][match.group(2)] = {}
        d[key][match.group(2)][match.group(1)] = match.group(3)
    return d


#don't run on import
if __name__ == '__main__':
    with open('sh_cdp_n_sw1.txt') as src:
        command = src.read()
    print(parse_sh_cdp_neighbors(command))
