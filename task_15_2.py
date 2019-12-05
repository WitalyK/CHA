# -*- coding: utf-8 -*-
'''
Задание 15.2
Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br
Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol
Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]
Для получения такого результата, используйте регулярные выражения.
Проверить работу функции на примере файла sh_ip_int_br.txt.
'''

from re import finditer

def parse_sh_ip_int_br(command_filename):
    regex = (r'(?P<interface>\S+) +(?P<ip>\S+).+(?P<status>(?:up|administratively down)) +(?P<protocol>(?:up|down))')
    with open(command_filename) as cfg:
        match_iter = finditer(regex, cfg.read())
    return [match.groups() for match in match_iter]

# don't run on import
if __name__ == '__main__':
    print(parse_sh_ip_int_br('sh_ip_int_br.txt'))