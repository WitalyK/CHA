# -*- coding: utf-8 -*-
'''
Задание 4.3

Создать класс Topology, который представляет топологию сети.
Класс Topology должен наследовать абстрактный класс MutableMapping
и для всех абстрактных методов класса MutableMapping должна быть
написана рабочая реализация в классе Topology.

Проверить, что после реализации абстрактных методов, работают также
такие методы: keys, items, values, get, pop, popitem, clear, update, setdefault.

При создании экземпляра класса, как аргумент передается словарь, который описывает топологию.
В каждом экземпляре должна быть создана переменная topology, в которой
содержится словарь топологии.

Пример создания экземпляра класса:
In [1]: t1 = Topology(example1)

In [2]: t1.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Проверка реализации абстрактных методов:

получение элемента:
In [3]: t1[('R1', 'Eth0/0')]
Out[3]: ('SW1', 'Eth0/1')


Перезапись/добавление элемента:
In [5]: t1[('R1', 'Eth0/0')] = ('SW1', 'Eth0/12')

In [6]: t1.topology
Out[6]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/12'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [7]: t1[('R6', 'Eth0/0')] = ('SW1', 'Eth0/17')

In [8]: t1.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/12'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
 ('R6', 'Eth0/0'): ('SW1', 'Eth0/17')}


Удаление:
In [11]: del t1[('R6', 'Eth0/0')]

In [12]: t1.topology
Out[12]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/12'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Итерация:
In [13]: for item in t1:
    ...:     print(item)
    ...:
('R1', 'Eth0/0')
('R2', 'Eth0/0')
('R2', 'Eth0/1')
('R3', 'Eth0/0')
('R3', 'Eth0/1')
('R3', 'Eth0/2')

Длина:
In [14]: len(t1)
Out[14]: 6

После реализации абстрактных методов, должны работать таким методы:

In [1]: t1.topology
Out[1]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

keys, values, items:
In [2]: t1.keys()
Out[2]: KeysView(<__main__.Topology object at 0xb562f82c>)

In [3]: t1.values()
Out[3]: ValuesView(<__main__.Topology object at 0xb562f82c>)

Метод get:
In [4]: t1.get(('R2', 'Eth0/0'))
Out[4]: ('SW1', 'Eth0/2')

In [6]: print(t1.get(('R2', 'Eth0/4')))
None

Метод pop:
In [8]: t1.pop(('R2', 'Eth0/0'))
Out[8]: ('SW1', 'Eth0/2')

In [9]: t1.topology
Out[9]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Метод update:
In [10]: t2.topology
Out[10]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

In [11]: t1.update(t2)

In [13]: t1.topology
Out[13]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

Метод clear:
In [14]: t1.clear()

In [15]: t1.topology
Out[15]: {}

'''
from pprint import pprint
from collections.abc import MutableMapping


class Topology(MutableMapping):
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology):
        d = {}
        for key, value in topology.items():
            if key < value:
                d[key] = value
            else:
                d[value] = key
        return d
        # dd = topology.copy()
        # ddd = topology.copy()
        # for key, value in topology.items():
        #     is_dubl = False
        #     for key1, value1 in dd.items():
        #         if key == value1 and value == key1:
        #             is_dubl = True
        #             break
        #     if key in dd: del dd[key]
        #     if is_dubl:
        #         del dd[value]
        #         del ddd[value]
        # return ddd

    def delete_link(self, host1, host2):
        if self.topology.get(host1, None) == host2:
            del self.topology[host1]
            return
        if self.topology.get(host2, None) == host1:
            del self.topology[host2]
            return
        print('Такого соединения нет')

    def delete_node(self, host):
        keys = [key for key, value in self.topology.items()
                if key[0] == host or value[0] == host]
        if keys:
            for key in keys:
                del self.topology[key]
        else:
            print('Такого устройства нет')

    def add_link(self, link1, link2):
        if (self.topology.get(link1, None) == link2) or (self.topology.get(link2, None) == link1):
            print('Такое соединение существует')
        elif (link1 in self.topology.keys()) or (link2 in self.topology.keys()) \
            or (link1 in self.topology.values()) or (link2 in self.topology.values()):
            print('Cоединение с одним из портов существует')
        else:
            self.topology[link1] = link2

    def __add__(self, other):
        d = self.topology.copy()
        d.update(other.topology)
        return Topology(d)

    def __iter__(self):
        items = (key for key in self.topology)
        return iter(items)

    def __getitem__(self, key):
        if self.topology.get(key):
            return self.topology[key]
        else:
            for k, value in self.topology.items():
                if value == key:
                    return k

    def __setitem__(self, key, value):
        if key < value:
            self.topology[key] = value
        else:
            self.topology[value] = key

    def __len__(self):
        return len(self.topology)

    def __delitem__(self, key):
        if self.topology.get(key):
            del self.topology[key]
        else:
            for k, value in self.topology.items():
                if value == key:
                    key1 = k
                    break
            del self.topology[key1]


# don't run on import
if __name__ == "__main__":
    example1 = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                ('R4', 'Eth0/0'): ('R3', 'Eth0/1'),
                ('R5', 'Eth0/0'): ('R3', 'Eth0/2')}

    example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
    t1 = Topology(example1)
    t2 = Topology(example2)
    t3 = t1 + t2
    pprint(t1.topology, width=40)
    pprint(t2.topology, width=40)
    pprint(t3.topology, width=40)
    print('*' * 45)
    print(t1[('R1', 'Eth0/0')])
    t1[('R1', 'Eth0/0')] = ('SW1', 'Eth0/12')
    print('*' * 45)
    print(t1[('R1', 'Eth0/0')])
    print('*' * 45)
    t1[('R6', 'Eth0/0')] = ('SW1', 'Eth0/17')
    pprint(t1.topology, width=40)
    print('*' * 45)
    del t1[('R6', 'Eth0/0')]
    pprint(t1.topology, width=40)
    print('*' * 45)
    for item in t1:
        print(item)
    print('*' * 45)
    print(len(t1))
    print('*' * 45)
    print(t1.keys())
    print(t1.values())
    print(t1.items())
    print(t1.get(('R2', 'Eth0/0')))
    print('*' * 45)
    print(t1.get(('R2', 'Eth0/4')))
    print('*' * 45)
    print(t1.pop(('R2', 'Eth0/0')))
    print('*' * 45)
    t1.update(t2)
    pprint(t1.topology, width=40)
    print('*' * 45)
    print(len(t1))
    print('*' * 45)
    t1.clear()
    pprint(t1.topology, width=40)

