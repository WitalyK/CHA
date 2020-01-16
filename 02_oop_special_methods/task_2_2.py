# -*- coding: utf-8 -*-
'''
Задание 2.2

Скопировать класс PingNetwork из задания 1.2 и изменить его таким образом,
чтобы адреса пинговались не при вызове метода scan, а при вызове экземпляра.

Вся функциональность метода scan должна быть перенесена в метод, который отвечает
за вызов экземпляра.

Пример работы с классом PingNetwork. Сначала создаем сеть:
In [2]: net1 = IPv4Network('8.8.4.0/29')

И выделяем несколько адресов:
In [3]: net1.allocate('8.8.4.2')
   ...: net1.allocate('8.8.4.4')
   ...: net1.allocate('8.8.4.6')
   ...:

Затем создается экземпляр класса PingNetwork, сеть передается как аргумент:
In [6]: ping_net = PingNetwork(net1)

После этого экземпляр должен быть вызываемым объектом (callable):

In [7]: ping_net()
Out[7]: (['8.8.4.4'], ['8.8.4.2', '8.8.4.6'])

In [8]: ping_net(include_unassigned=True)
Out[8]: (['8.8.4.4'], ['8.8.4.2', '8.8.4.6', '8.8.4.1', '8.8.4.3', '8.8.4.5'])


'''
from task_1_1 import IPv4Network
import subprocess
from datetime import datetime
from re import findall
from concurrent.futures import ThreadPoolExecutor, as_completed


class PingNetwork:
    def __init__(self, net):
        self.net = net

    def _ping(self, ip):
        regex = r'.+ TTL=.+'
        result = subprocess.run(['ping', '-n', '2', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if findall(regex, result.stdout.decode('cp866')):
            return True
        else:
            return False

    def _awailable(self, ip):
        return self._ping(ip), ip

    def __call__(self, workers=5, include_unassigned=False):
        awailable_ip = []
        unawailable_ip = []
        if include_unassigned:
            ip_list = self.net.hosts()
        else:
            ip_list = self.net.allocated
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(self._awailable, ip) for ip in ip_list]
            for f in as_completed(futures):
                try:
                    if f.result()[0]:
                        awailable_ip.append(f.result()[1])
                    else:
                        unawailable_ip.append(f.result()[1])
                except:
                    print('Error')
        return sorted(awailable_ip), sorted(unawailable_ip)


# don't run on import
if __name__ == "__main__":
    start_time = datetime.now()
    net1 = IPv4Network('8.8.4.0/29')
    net1.allocate('8.8.4.2')
    net1.allocate('8.8.4.4')
    net1.allocate('8.8.4.6')
    ping_net = PingNetwork(net1)
    print(ping_net())
    print('*'*45)
    print(ping_net(include_unassigned=True))
    print(datetime.now() - start_time)
