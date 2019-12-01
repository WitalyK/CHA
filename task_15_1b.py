# -*- coding: utf-8 -*-
'''
Задание 15.1b
Проверить работу функции get_ip_from_cfg из задания 15.1a на конфигурации config_r2.txt.
Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary
А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).
Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким образом,
чтобы в значении словаря она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.
Ключом остается имя интерфейса.
Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.
Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.
'''
from re import finditer

def get_ip_from_cfg(cfg_filename):
    regex = (r'interface (?P<interface>\S+)'
             r'| ip address (?P<ip>(?:\d+\.){3}\d+) +(?P<mask>(?:\d+\.){3}\d+)')
    result = {}
    with open(cfg_filename) as cfg:
        match_iter = finditer(regex, cfg.read())
        for match in match_iter:
            if match.lastgroup == 'interface':
                interface = match.group(match.lastgroup)
                intf =[]
            else:
                intf.append((match.group('ip'), match.group('mask')))
                result[interface] = intf
    return result

# don't run on import
if __name__ == "__main__":
    print(get_ip_from_cfg('config_r2.txt'))

#    r'interface (\S+)(?:(?:(?!interface).)*\n)+? ip address ((?:\d+\.){3}\d+) +((?:\d+\.){3}\d+)'
