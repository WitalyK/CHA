# -*- coding: utf-8 -*-
'''
Задание 17.2b
Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.
Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.
Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}
Функция transform_topology должна не только менять формат представления топологии,
но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).
Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать
изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.
Результат должен выглядеть так же, как схема в файле task_17_2b_topology.svg
При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков
> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz
> И модуль python для работы с graphviz:
> pip install graphviz
'''
# from draw_network_graph import draw_topology
import yaml
from pprint import pprint


def transform_topology(yaml_file):
    with open(yaml_file) as src:
        templates = yaml.safe_load(src)
    d = {}
    for d_in, value in templates.items():
        for int_in, value_in in value.items():
            for d_out, int_out in value_in.items():
                d[(d_in, int_in)] = (d_out, int_out)
    for key in set(d):
        if (key, d[key]) in list(zip(d.values(), d.keys())):
            del d[key]
    # dd = d.copy()
    # ddd = d.copy()
    # for key, value in d.items():
    #     is_dubl = False
    #     for key1, value1 in dd.items():
    #         if key==value1 and value==key1:
    #             is_dubl = True
    #             break
    #     if key in dd: del dd[key]
    #     if is_dubl:
    #         del dd[value]
    #         del ddd[value]
    return d


# don't run on import
if __name__ == '__main__':
    # draw_topology(transform_topology('topology.yaml'))
    pprint(transform_topology('topology.yaml'))
    # transform_topology('topology.yaml')
