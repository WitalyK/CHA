# -*- coding: utf-8 -*-
"""
Задание 8.1b

Создать генератор get_intf_ip_from_files, который ожидает как аргумент
произвольное количество файлов с конфигурацией устройств и возвращает интерсейсы и IP-адреса,
которые настроены на интерфейсах.

Генератор должен обрабатывать конфигурацию и возвращать словарь
для каждого файла на каждой итерации:

* ключ - hostname (надо получить из конфигурационного файла из строки hostname ...)
* значение словарь, в котором:
    * ключ - имя интерфейса
    * значение - кортеж с IP-адресом и маской

Например: {'r1': {'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
                  'FastEthernet0/2': ('10.0.2.2', '255.255.255.0')}}

Проверить работу генератора на примере конфигураций config_r1.txt и config_r2.txt.

"""
import re
from pprint import pprint


def get_intf_ip_from_files(*filenames):
    for filename in filenames:
        with open(filename) as f:
            d = {}
            host = True
            for line in f:
                if host:
                    match = re.match('hostname (\S+)', line)
                    if match:
                        host = False
                        hostname = match.group(1)
                        d[hostname] = {}
                else:
                    match = re.match('interface (\S+)', line)
                    if match:
                        interface = match.group(1)
                    else:
                        match = re.match(' ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)', line)
                        if match:
                            d[hostname][interface] = (match.group(1), match.group(2))
            yield d


# don't run on import
if __name__ == "__main__":
    for n in get_intf_ip_from_files('config_r1.txt', 'config_r2.txt'):
        pprint(n)