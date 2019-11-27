# -*- coding: utf-8 -*-
'''
Задание 12.2
Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.
В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.
Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.
Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10
Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.
Функция возвращает список IP-адресов.
Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']
'''
from ip_ch import ip_correct
from task_12_1 import ping_ip_addresses
from ipaddress import ip_address


def convert_ranges_to_ip_list(ip_diapazon_list):
    ip_list = []
    for ip_or_diap in ip_diapazon_list:
        if '-' in ip_or_diap:
            is_short = len(ip_or_diap.split('.')) == 4
            l = ip_or_diap.split('-')
            if is_short: d2 = int(l[1])
            else: d2 = int(l[1].split('.')[3])
            dia = d2 - int(l[0].split('.')[3])
            ip1= ip_address(l[0])
            ip_list += [str(ip1+n) for n in range(dia+1)]
        else:
            ip_list.append(ip_or_diap)
    return ip_list


#не запускать при импорте
if __name__ == "__main__":
    diapazon_list = []
    while True:
        ip_or_diapazon = input(': ')
        if ip_or_diapazon == ' ':
            break
        diapazon_list.append(ip_or_diapazon)

    print(convert_ranges_to_ip_list(diapazon_list))

