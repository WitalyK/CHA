# -*- coding: utf-8 -*-
'''
Задание 3.2

Скопировать класс PingNetwork из задания 1.2.
Один из методов класса зависит только от значения аргумента и не зависит
от значений переменных экземпляра или другого состояния объекта.

Сделать этот метод статическим и проверить работу метода.

'''
import subprocess
from re import findall
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from task_3_1 import IPv4Network
from tabulate import tabulate


class PingNetwork:
    def __init__(self, net):
        self.net = net

    @staticmethod
    def _ping(ip):
        regex = r'.+ TTL=.+'
        result = subprocess.run(['ping', '-n', '2', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if findall(regex, result.stdout.decode('cp866')):
            return True
        else:
            return False

    @staticmethod
    def _awailable(ip):
        return PingNetwork._ping(ip), ip

    def scan(self, workers=5, include_unassigned=False):
        awailable_ip = []
        unawailable_ip = []
        if include_unassigned:
            ip_list = self.net.hosts
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


def prepare_for_tabulate(list_awailable_ip, list_unawailable_ip):
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
    net1 = IPv4Network('8.8.4.0/29')
    net1.allocate('8.8.4.2')
    net1.allocate('8.8.4.3')
    net1.allocate('8.8.4.4')
    print(net1.allocated)
    print(net1.unassigned)
    ping_net = PingNetwork(net1)
    tup = prepare_for_tabulate(*ping_net.scan(workers=18))
    print(tabulate(list(zip(tup[0], tup[1])), headers=['Reachable', 'Unreachable'], tablefmt='grid'))
    print('*' * 45)
    tup = prepare_for_tabulate(*ping_net.scan(workers=18, include_unassigned=True))
    print(tabulate(list(zip(tup[0], tup[1])), headers=['Reachable', 'Unreachable'], tablefmt='grid'))
    print(datetime.now() - start_time)
