# -*- coding: utf-8 -*-
'''
Задание 11.1
Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.
У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.
Функция должна возвращать словарь, который описывает соединения между устройствами.
Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors
Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0
Функция должна вернуть такой словарь:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.
Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def parse_cdp_neighbors(command_output):
    lines = command_output.split('\n')
    name = lines[0].split('>')[0]
    flag = False
    d = {}
    for line in lines:
        if flag and len(line.split())>1:
            di, in1, in2, *rest, po1, po2 = line.split()
            d[(name, in1+in2)] = (di, po1+po2)
        if line.startswith('Device'):
            flag = True
    return d


#не запускать при импорте
if __name__ == "__main__":
    with open('sh_cdp_n_sw1.txt') as src:
        command = src.read()

    print(parse_cdp_neighbors(command))