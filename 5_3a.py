# -*- coding: utf-8 -*-
'''
в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'
'''
access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]
access_template = ['Введите номер VLAN: '] + access_template

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
trunk_template = ['Введите разрешенные VLANы: '] + trunk_template

modes = {'access': access_template, 'trunk': trunk_template}

m = input('Введите режим работы интерфейса (access/trunk): ')
intf = input('Введите тип и номер интерфейса: ')
vlans = input(modes[m][0])
mm = '\n'.join(modes[m])
print('interface ', intf)
print(mm.format(vlans))