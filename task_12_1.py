# -*- coding: utf-8 -*-
'''
Задание 12.1
Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.
Функция ожидает как аргумент список IP-адресов.
Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов
Для проверки доступности IP-адреса, используйте ping.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess


def ping_ip_addresses(ip_list):
    awailable_ip = []
    unawailable_ip =[]
    for ip in ip_list:
        print('Check address ', ip)
        result = subprocess.run(['ping', '-n', '2', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if result.returncode == 0:
            awailable_ip.append(ip)
        else:
            unawailable_ip.append(ip)
    return awailable_ip, unawailable_ip

#не запускать при импорте
if __name__ == "__main__":
    ip_address_list = ['10.1.1.1', '10.111.111.2', '10.111.111.3', '10.20.10.2', '10.11.11.11', '10.111.111.4', '10.111.10.1', '10.111.222.2', '10.111.10.2', '1.1.1.1']
    print(ping_ip_addresses(ip_address_list))