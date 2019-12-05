# -*- coding: utf-8 -*-
from sys import argv
'''
Задание 7.2
Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту
Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.
Между строками не должно быть дополнительного символа перевода строки.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ff = argv[1]
#ff = 'config_sw1.txt'
ignore = ['duplex', 'alias', 'Current configuration']
with open(ff) as f:
    for line in f:
        if (not line.startswith("!")) and (not any([word in line for word in ignore])):
            print(line.rstrip('\n'))

