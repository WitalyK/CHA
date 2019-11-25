# -*- coding: utf-8 -*-
import os
'''
Задание 9.3
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}
* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}
У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1
В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }
'''
def get_int_vlan_map(config_filename):
    if os.path.exists(config_filename):
        with open(config_filename) as src:
            access_d = {}
            trunk_d = {}
            for line in src:
                if 'interface' in line:
                    i = line.split()[1]
                if 'switchport mode access' in line:
                    access_flag = True
                if 'access vlan' in line:
                    v = int(line.split()[3])
                    access_d[i] = v
                    access_flag = False
                if 'duplex auto' in line and access_flag:
                    access_d[i] = 1
                    access_flag = False
                if 'trunk allowed vlan' in line:
                    v = line.split()[4].split(',')
                    v = [int(s) for s in v]
                    trunk_d[i] = v
        return access_d, trunk_d
    else:
        print("Нет такого файла")
        return False


print(get_int_vlan_map('config_sw2.txt'))