# -*- coding: utf-8 -*-
'''
Задание 21.5

Создать шаблоны templates/gre_ipsec_vpn_1.txt и templates/gre_ipsec_vpn_2.txt,
которые генерируют конфигурацию IPsec over GRE между двумя маршрутизаторами.

Шаблон templates/gre_ipsec_vpn_1.txt создает конфигурацию для одной стороны туннеля,
а templates/gre_ipsec_vpn_2.txt - для второй.

Примеры итоговой конфигурации, которая должна создаваться на основе шаблонов в файлах:
cisco_vpn_1.txt и cisco_vpn_2.txt.


Создать функцию create_vpn_config, которая использует эти шаблоны для генерации конфигурации VPN
на основе данных в словаре data.

Параметры функции:
* template1 - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* template2 - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна возвращать кортеж с двумя конфигурациямя (строки), которые получены на основе шаблонов.

Примеры конфигураций VPN, которые должна возвращать функция create_vpn_config в файлах
cisco_vpn_1.txt и cisco_vpn_2.txt.
'''
import jinja2
import os


def create_temppate(template, d_dict):
    template_dir, template_file = os.path.split(template)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                             trim_blocks=True, lstrip_blocks=True)
    return env.get_template(template_file).render(d_dict)

def create_vpn_config(template1, template2, data_dict):
    return create_temppate(template1, data_dict), create_temppate(template2, data_dict)

#don't run on import
if __name__ == "__main__":
    data = {
        'tun_num': 10,
        'wan_ip_1': '10.111.111.11',
        'wan_ip_2': '10.111.111.3',
        'tun_ip_1': '10.0.1.1 255.255.255.252',
        'tun_ip_2': '10.0.1.2 255.255.255.252'
    }
    t = create_vpn_config("templates/gre_ipsec_vpn_1.txt", "templates/gre_ipsec_vpn_2.txt", data)
    for vpn_conf in t:
        print(vpn_conf)