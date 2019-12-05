# -*- coding: utf-8 -*-
'''
Задание 7.1
Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0
Ограничение not
'''
import re

templ = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface:']
with open('ospf.txt') as f:
    for line in f:
        line = line.replace('O', 'OSPF')
        str1 = re.split(r'(?:via|[\[\] ,])+', line)
        i=0
        for s in str1:
            print('{:<23} {}'.format(templ[i], s))
            i += 1
        print('----------------')
print('****************************')