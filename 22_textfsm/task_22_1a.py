# -*- coding: utf-8 -*-
'''
Задание 22.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
'''
import textfsm

def parse_output_to_dict(template, command_output):
    with open(template) as templ:
        re_table = textfsm.TextFSM(templ)
        header = re_table.header
        result = re_table.ParseText(command_output)
    return [dict(zip(header, res)) for res in result]

# don't run on import
if __name__ == "__main__":
    with open('output/sh_ip_int_br.txt') as f:
        list_dict = parse_output_to_dict('templates/sh_ip_int_br.template', f.read())
        for line in list_dict:
            print(line)