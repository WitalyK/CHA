# -*- coding: utf-8 -*-
from sys import argv

'''
Задание 7.3b
Сделать копию скрипта задания 7.3a.
Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.
 '''
vlan = int(input('Введите номер VLAN: '))
with open('CAM_table.txt') as src:
    list = []
    for line in src:
        if len(line.split('.')) == 3:
            vlans, mac, _, inf = line.split()
            if int(vlans) == vlan:
                list.append([int(vlans), mac, inf])
    list.sort(key=lambda x: x[-1])
    [print('{:<6} {:<18} {}'.format(line[0], line[1], line[2])) for line in list]
