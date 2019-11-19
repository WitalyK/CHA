# -*- coding: utf-8 -*-

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

modes = {'access': access_template, 'trunk': trunk_template}

m = input('Введите режим работы интерфейса (access/trunk): ')
intf = input('Введите тип и номер интерфейса: ')
vlans = input('Введите номер влан(ов): ')
mm = '\n'.join(modes[m])
print('interface ', intf)
print(mm.format(vlans))
