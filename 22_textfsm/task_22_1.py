# -*- coding: utf-8 -*-
'''
Задание 22.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
'''
import textfsm

def parse_command_output(template, command_output):
    with open(template) as templ:
        re_table = textfsm.TextFSM(templ)
        header = re_table.header
        result = re_table.ParseText(command_output)
        result.insert(0, header)
    return result

# don't run on import
if __name__ == "__main__":
    with open('output/sh_ip_int_br.txt') as f:
        parse_otput_list = parse_command_output("templates/sh_ip_int_br.template", f.read())
    for line in parse_otput_list:
        print(line)
