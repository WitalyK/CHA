# -*- coding: utf-8 -*-
'''
Задание 9.2
Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов.
У функции должны быть такие параметры:
- intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
- trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде списка команд (список trunk_mode_template)
Функция должна возвращать список команд с конфигурацией
на основе указанных портов и шаблона trunk_mode_template.
В конце строк в списке не должно быть символа перевода строки.
Проверить работу функции на примере словаря trunk_config.
Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):
[
'interface FastEthernet0/1',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 10,20,30',
'interface FastEthernet0/2',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 11,30',
...]
Ограничение: Все задания надо выполнять используя только пройденные темы.


Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
'''

def generate_trunk_config(intf_vlan_mapping, trunk_template, psecurity = None):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    d = {}
    for key, value in intf_vlan_mapping.items():
        list2 = []
        for command in trunk_template:
            if command.endswith("vlan"):
                list2.append(command + ' ' + ' '.join([str(item) for item in value]))
            else:
                list2.append(command)
        if psecurity:
            for command in psecurity:
                list2.append(command)
        d[key] = list2
    return d


trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

print(generate_trunk_config(trunk_config, trunk_mode_template))