# -*- coding: utf-8 -*-

'''
Задание 25.1

Создать класс Topology, который представляет топологию сети.

При создании экземпляра класса, как аргумент передается словарь, который описывает топологию.
Словарь может содержать дублирующиеся соединения.

Дублем считается ситуация, когда в словаре есть такие пары:
    ('R1', 'Eth0/0'): ('SW1', 'Eth0/1') и ('SW1', 'Eth0/1'): ('R1', 'Eth0/0')

В каждом экземпляре должна быть создана переменная topology, в которой содержится словарь топологии, но уже без дублей.

Пример создания экземпляра класса:
In [2]: top = Topology(topology_example)

После этого, должна быть доступна переменная topology:

In [3]: top.topology
Out[3]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}


'''
from pprint import pprint


class Topology:
    def __init__(self, topology):
        dd = topology.copy()
        ddd = topology.copy()
        for key, value in topology.items():
            is_dubl = False
            for key1, value1 in dd.items():
                if key==value1 and value==key1:
                    is_dubl = True
                    break
            if key in dd: del dd[key]
            if is_dubl:
                del dd[value]
                del ddd[value]
        self.topology = ddd
        
#don't run on import
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
    top = Topology(topology_example)
    pprint(top.topology, width=120)

