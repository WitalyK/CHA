# -*- coding: utf-8 -*-
'''
Задание 3.1

Скопировать класс IPv4Network из задания 1.1.
Переделать класс таким образом, чтобы методы hosts и unassigned
стали переменными, но при этом значение переменной экземпляра вычислялось
каждый раз при обращении и запись переменной была запрещена.


Пример создания экземпляра класса:
In [1]: net1 = IPv4Network('8.8.4.0/29')

In [2]: net1.hosts
Out[2]: ('8.8.4.1', '8.8.4.2', '8.8.4.3', '8.8.4.4', '8.8.4.5', '8.8.4.6')

In [3]: net1.allocate('8.8.4.2')

In [4]: net1.allocate('8.8.4.3')

In [5]: net1.unassigned
Out[5]: ('8.8.4.1', '8.8.4.4', '8.8.4.5', '8.8.4.6')

Запись переменной:

In [6]: net1.unassigned = 'test'
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-c98e898835e1> in <module>
----> 1 net1.unassigned = 'test'

AttributeError: can't set attribute

'''
from ipaddress import ip_network


class IPv4Network:
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

    # optional
    def __iter__(self):
        return iter(self.hosts)

    # optional
    def __contains__(self, item):
        return item in self.hosts

    def index(self, value):
        return self.hosts.index(value)

    def count(self, value):
        return self.hosts.count(value)


# don't run on import
if __name__ == "__main__":
    net1 = IPv4Network('8.8.4.0/29')
    print(net1.hosts)
    print('*'*45)
    net1.allocate('8.8.4.2')
    net1.allocate('8.8.4.3')
    print(net1.unassigned)
    print('*'*45)
    net1.unassigned = 'test'
