# -*- coding: utf-8 -*-
'''
Задание 15.1a
Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска
В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.
Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}
Для получения такого результата, используйте регулярные выражения.
Проверить работу функции на примере файла config_r1.txt.
Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.
'''

from  re import findall

def get_ip_from_cfg(cfg_filename):
    with open(cfg_filename) as cfg:
        cfg_str = cfg.read()
    d = {}
#    for key, ip, mask in findall('interface (\S+)(?:(?:(?!interface).)*\n)+? ip address ((?:\d+\.){3}\d+) +((?:\d+\.){3}\d+)', cfg_str):
#        d[key] = (ip, mask)
    return  {key: (ip, mask) for key, ip, mask in
             findall(r'interface (\S+)(?:(?:(?!interface).)*\n)+? ip address ((?:\d+\.){3}\d+) +((?:\d+\.){3}\d+)', cfg_str)}

#interface Loopback0

# don't run on import
if __name__ == "__main__":
    print(get_ip_from_cfg('config_r1.txt'))