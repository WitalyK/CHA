# -*- coding: utf-8 -*-
from sys import path
path.append('d:/Python/CHA/CHA/')
from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology
'''
Задание 11.2
Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.
У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов,
в которых находится вывод команды show cdp neighbors.
Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
В словаре, который возвращает функция create_network_map, не должно быть дублей.
С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии,
полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg
При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
Не копировать код функций parse_cdp_neighbors и draw_topology.
Ограничение: Все задания надо выполнять используя только пройденные темы.
> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz
> И модуль python для работы с graphviz:
> pip install graphviz
'''

def create_network_map(filenames):
    d = {}
    for file in filenames:
        with open(file) as src:
            d.update(parse_cdp_neighbors(src.read()))
    dd = d.copy()
    ddd = d.copy()
    for key, value in d.items():
        is_dubl = False
        for key1, value1 in dd.items():
            if key==value1 and value==key1:
                is_dubl = True
                break
        if key in dd: del dd[key]
        if is_dubl:
            del dd[value]
            del ddd[value]
    return ddd

files = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']
draw_topology(create_network_map(files))
