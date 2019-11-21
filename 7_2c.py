# -*- coding: utf-8 -*-
from sys import argv

'''
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации
Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.
Проверить работу скрипта на примере файла config_sw1.txt.
'''

ignore = ['duplex', 'alias', 'Current configuration']
with open(argv[1]) as src, open(argv[2], 'w') as dst:
    for line in src:
        is_ignore = True
        for s in ignore:
            if s in line:
                is_ignore = False
                break
        if is_ignore:
            dst.write(line)

