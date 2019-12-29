# -*- coding: utf-8 -*-
'''
Задание 22.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами.
Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - templates

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
'''
from textfsm import clitable


def parse_command_dynamic(command_output, attributes_dict, index_file="index", templ_path="templates"):
    cli = clitable.CliTable(index_file, templ_path)
    cli.ParseCmd(command_output, attributes_dict)
    header = list(cli.header)
    return [dict(zip(header, list(res))) for res in cli]

# don't run on import
if __name__ == "__main__":
    attributes = {'Command': "sh ip int br", 'Vendor': "cisco_ios"}
    with open("output/sh_ip_int_br.txt") as f:
        list_dict = parse_command_dynamic(f.read(), attributes)
        for line in list_dict:
            print(line)