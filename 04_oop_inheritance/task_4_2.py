# -*- coding: utf-8 -*-
'''
Задание 4.2

Скопировать класс IPv4Network из задания 3.1 и изменить его таким
образом, чтобы класс IPv4Network наследовал абстрактный класс Sequence.
Создать все необходимые абстрактные методы для работы IPv4Network как Sequence.

Проверить, что работают все методы характерные для последовательности (sequence):
* __getitem__, __len__, __contains__, __iter__, index, count

Пример создания экземпляра класса:

In [1]: net1 = IPv4Network('8.8.4.0/29')

Проверка методов:

In [2]: len(net1)
Out[2]: 6

In [3]: net1[0]
Out[3]: '8.8.4.1'

In [4]: '8.8.4.1' in net1
Out[4]: True

In [5]: '8.8.4.10' in net1
Out[5]: False

In [6]: net1.count('8.8.4.1')
Out[6]: 1

In [7]: net1.index('8.8.4.1')
Out[7]: 0

In [8]: for ip in net1:
   ...:     print(ip)
   ...:
8.8.4.1
8.8.4.2
8.8.4.3
8.8.4.4
8.8.4.5
8.8.4.6

'''
from ipaddress import ip_network
from collections.abc import Sequence


class IPv4Network(Sequence):
    def __init__(self, net_addr):
        self.address, self.mask = net_addr.split('/')
        self.subnet = ip_network(net_addr)
        self.broadcast = str(self.subnet.broadcast_address)
        self.allocated = ()

    @classmethod
    def from_tuple(cls, t):
        return cls(t[0]+'/'+str(t[1]))

    @property
    def hosts(self):
        return tuple(str(host) for host in self.subnet.hosts())

    def allocate(self, ip_addr):
        if ip_addr in self.hosts:
            self.allocated += (ip_addr,)

    @property
    def unassigned(self):
        return tuple(host for host in self.hosts if host not in self.allocated)

    def __str__(self):
        return f'IPv4Network {self.address}/{self.mask}'

    def __repr__(self):
        return f"IPv4Network('{self.address}/{self.mask}')"

    def __len__(self):
        return len(self.hosts)

    def __getitem__(self, item):
        return self.hosts[item]

    # # optional
    # def __iter__(self):
    #     return iter(self.hosts)
    #
    # # optional
    # def __contains__(self, item):
    #     return item in self.hosts
    #
    # def index(self, value):
    #     return self.hosts.index(value)
    #
    # def count(self, value):
    #     return self.hosts.count(value)


# don't run on import
if __name__ == "__main__":
    net1 = IPv4Network('8.8.4.0/29')
    print(len(net1))
    print('*' * 45)
    print(net1[0])
    print('*' * 45)
    print('8.8.4.1' in net1)
    print('*' * 45)
    print('8.8.4.10' in net1)
    print('*' * 45)
    print(net1.count('8.8.4.1'))
    print('*' * 45)
    print(net1.index('8.8.4.1'))
    print('*' * 45)
    for ip in net1:
        print(ip)
    i = iter(net1)
    print('*' * 45)
    print(next(i))
    print(next(i))
    print('*' * 45)
    print(list(reversed(net1)))