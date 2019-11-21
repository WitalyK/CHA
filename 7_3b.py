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
            s = line.split()
            if int(s[0]) == vlan:
                list.append([int(s[0]), s[1], s[3]])
    list.sort()
    s = ''
    for line in list:
        s = s + '{:<6} {:<18} {}'.format(line[0], line[1], line[2]) + '\n'
    print(s)
