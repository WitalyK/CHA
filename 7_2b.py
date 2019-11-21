# -*- coding: utf-8 -*-
from sys import argv
'''
Задание 7.2b
Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt
При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ff = argv[1]
ignore = ['duplex', 'alias', 'Current configuration']
with open(ff) as src, open('config_sw1_cleared.txt', 'w') as dst:
    for line in src:
        is_ignore = True
        for s in ignore:
            if s in line:
                is_ignore = False
                break
        if is_ignore:
            dst.write(line)

