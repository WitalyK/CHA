# -*- coding: utf-8 -*-
'''
Задание 1.2

Создать класс PingNetwork. При создании экземпляра класса PingNetwork, как аргумент передается экземпляр класса IPv4Network.

У класса PingNetwork должны быть методы _ping и scan

Метод _ping с параметром ip: должен пинговать один IP-адрес и возвращать
* True - если адрес пингуется
* False - если адрес не пингуется

Метод scan с таким параметрами:

* workers - значение по умолчанию 5
* include_unassigned - значение по умолчанию False

Метод scan:

* Пингует адреса из сети, которая передается как аргумент при создании экземпляра.
* Адреса должны пинговаться в разных потоках, для этого использовать concurrent.futures.
* По умолчанию, пингуются только адреса, которые находятся в атрибуте allocated.
  Если параметр include_unassigned равен True, должны пинговаться и адреса unassigned.
* Метод должен возвращать кортеж с двумя списками: список доступных IP-адресов и список недоступных IP-адресов



Пример работы с классом PingNetwork. Сначала создаем сеть:
In [3]: net1 = IPv4Network('8.8.4.0/29')

И выделяем несколько адресов:
In [4]: net1.allocate('8.8.4.2')
   ...: net1.allocate('8.8.4.4')
   ...: net1.allocate('8.8.4.6')
   ...:

In [5]: net1.allocated
Out[5]: ('8.8.4.2', '8.8.4.4', '8.8.4.6')

In [6]: net1.unassigned()
Out[6]: ('8.8.4.1', '8.8.4.3', '8.8.4.5')

Затем создается экземпляр класса PingNetwork, а сеть передается как аргумент:

In [8]: ping_net = PingNetwork(net1)

Пример работы метода scan:
In [9]: ping_net.scan()
Out[9]: (['8.8.4.4'], ['8.8.4.2', '8.8.4.6'])

In [10]: ping_net.scan(include_unassigned=True)
Out[10]: (['8.8.4.4'], ['8.8.4.2', '8.8.4.6', '8.8.4.1', '8.8.4.3', '8.8.4.5'])

'''
from task_1_1 import IPv4Network
import subprocess, logging
from datetime import datetime
from re import findall
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(
    format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


class PingNetwork:
    def __init__(self, net):
        self.net = net

    def _ping(self, ip):
        logging.info(' ==> Check address ' + ip)
        regex = (r'.+ TTL=.+')
        result = subprocess.run(['ping', '-n', '2', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        logging.info(' <== Checked address ' + ip)
        if findall(regex, result.stdout.decode('cp866')):
            return True
        else:
            return False

    def _awailable(self, ip):
        return self._ping(ip), ip

    def scan(self, workers=5, include_unassigned=False):
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


def prepare_for_tabulate(t):
    list_awailable_ip, list_unawailable_ip = t
    awa_len = len(list_awailable_ip)
    unawa_len = len(list_unawailable_ip)
    if awa_len != unawa_len:
        if awa_len > unawa_len:
            [list_unawailable_ip.append('') for i in range(awa_len - unawa_len)]
        else:
            [list_awailable_ip.append('') for i in range(unawa_len - awa_len)]
    return list_awailable_ip, list_unawailable_ip


# don't run on import
if __name__ == "__main__":
    start_time = datetime.now()
    net1 = IPv4Network('10.111.111.0/28')
    net1.allocate('10.111.111.2')
    net1.allocate('10.111.111.3')
    net1.allocate('10.111.111.7')
    print(net1.allocated)
    print(net1.unassigned())
    ping_net = PingNetwork(net1)
    tup = prepare_for_tabulate(ping_net.scan(workers=18))
    print(tabulate(list(zip(tup[0], tup[1])), headers=['Reachable', 'Unreachable'], tablefmt='grid'))
    print('*' * 45)
    tup = prepare_for_tabulate(ping_net.scan(workers=18, include_unassigned=True))
    print(tabulate(list(zip(tup[0], tup[1])), headers=['Reachable', 'Unreachable'], tablefmt='grid'))
    print(datetime.now() - start_time)
