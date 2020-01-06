# -*- coding: utf-8 -*-

'''
Задание 25.1a

Скопировать класс Topology из задания 25.1 и изменить его.

Если в задании 25.1 удаление дублей выполнялось в методе __init__,
надо перенести функциональность удаления дублей в метод _normalize.

При этом метод __init__ должен выглядеть таким образом:
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
    top = Topology(topology_example)
    pprint(top.topology, width=120)
