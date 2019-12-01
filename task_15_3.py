# -*- coding: utf-8 -*-
'''
Задание 15.3
Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.
Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA
Функция ничего не возвращает.
Проверить функцию на файле cisco_nat_config.txt.
Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023
И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023
В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел
Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
'''
from re import finditer


def convert_ios_nat_to_asa(nat_cisco_ios, nat_cisco_asa):
    regex = (r'ip nat inside source (?P<stat>\S+) +(?P<prot>\S+) +(?P<ip>\S+) +(?P<portin>\S+) +(?P<intf>\S+).+ (?P<portout>\S+)')
    with open(nat_cisco_ios) as src:
        ios_nat = finditer(regex, src.read())
    with open(nat_cisco_asa, 'w') as dest:
        for match in ios_nat:
            dest.write('object network LOCAL_{}'.format(match.group('ip'))+'\n')
            dest.write(' host {}'.format(match.group('ip')) + '\n')
            dest.write(' nat (inside,outside) {} {} service {} {} {}'.format(match.group('stat'), match.group('intf'), match.group('prot'), match.group('portin'), match.group('portout')) + '\n')




#don't run on import
if __name__ == '__main__':
    convert_ios_nat_to_asa('cisco_nat_config.txt', 'cisco_asa_nat_config.txt')