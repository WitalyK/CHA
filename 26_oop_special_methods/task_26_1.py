# -*- coding: utf-8 -*-

'''
Задание 26.1

Изменить класс Topology из задания 25.1x.

Добавить метод, который позволит выполнять сложение двух объектов (экземпляров) Topology.
В результате сложения должен возвращаться новый экземпляр класса Topology.

Создание двух топологий:

In [1]: t1 = Topology(topology_example)

In [2]: t1.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [3]: topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                             ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

In [4]: t2 = Topology(topology_example2)

In [5]: t2.topology
Out[5]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

Суммирование топологий:

In [6]: t3 = t1+t2

In [7]: t3.topology
Out[7]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R1', 'Eth0/6'): ('R9', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Проверка, что исходные топологии не изменились:

In [9]: t1.topology
Out[9]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [10]: t2.topology
Out[10]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
'''
from pprint import pprint


class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology):
        dd = topology.copy()
        ddd = topology.copy()
        for key, value in topology.items():
            is_dubl = False
            for key1, value1 in dd.items():
                if key == value1 and value == key1:
                    is_dubl = True
                    break
            if key in dd: del dd[key]
            if is_dubl:
                del dd[value]
                del ddd[value]
        return ddd

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
        items = ((key, value) for key, value in self.topology.items())
        return iter(items)


# don't run on import
if __name__ == "__main__":
    topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                        ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                        ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                        ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                        ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                        ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                        ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                        ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                        ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}

    topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                         ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
    t1 = Topology(topology_example)
    t2 = Topology(topology_example2)
    t3 = t1 + t2
    pprint(t1.topology, width=40)
    pprint(t2.topology, width=40)
    pprint(t3.topology, width=40)
