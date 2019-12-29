# -*- coding: utf-8 -*-
'''
Задание 21.5a

Создать функцию configure_vpn, которая использует шаблоны из задания 21.5 для настройки VPN
на маршрутизаторах на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству
* dst_device_params - словарь с параметрами подключения к устройству
* src_template - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* dst_template - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов и данных на каждом устройстве.
Функция возвращает вывод с набором команд с двух марушртизаторов (вывод,
которые возвращает send_config_set).

При этом, в словаре data не указан номер интерфейса Tunnel, который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel, взять номер 0,
если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 9.
И надо будет настроить интерфейс Tunnel 9.

Для этого задания нет теста!
'''
import yaml, re, jinja2, netmiko, os
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
from concurrent.futures import ThreadPoolExecutor, as_completed

def create_temppate(template, d_dict):
    template_dir, template_file = os.path.split(template)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                             trim_blocks=True, lstrip_blocks=True)
    return env.get_template(template_file).render(d_dict)

def create_vpn_config(template1, template2, data_dict):
    return create_temppate(template1, data_dict), create_temppate(template2, data_dict)

def get_vpn_numbers(d):
    with netmiko.ConnectHandler(**d) as ssh:
        ssh.enable()
        res = ssh.send_command('sh ip int br | b Tun')
        result = []
        if res:
            result = re.findall(r'Tunnel(\d+) +', res)
        if result:
            result = [int(item) for item in result]
    return result

def get_vpn_number(devs):
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(get_vpn_numbers, dev) for dev in devs]
        tun_nums = set()
        for future in as_completed(futures):
            try:
                tun_nums.update(future.result())
            except (NetMikoAuthenticationException, NetMikoTimeoutException) as e:
                print(e)
    i = 0
    while True:
        if i not in tun_nums:
            break
        i += 1
    return i

def send_command_vpn(devv, command_list):
    with netmiko.ConnectHandler(**devv) as ssh:
        ssh.enable()
        res = ssh.send_config_set(command_list.split('\n'))
    return res

def configure_vpn(src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
    tun_num = get_vpn_number((src_device_params, dst_device_params))
    vpn_data_dict['tun_num'] = tun_num
    comm = create_vpn_config(src_template, dst_template, vpn_data_dict)
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(send_command_vpn, device, commands)
                   for device, commands in ((src_device_params, comm[0]), (dst_device_params, comm[1]))]
        t_futures = []
        for future in as_completed(futures):
            try:
                t_futures.append(future.result())
            except (NetMikoAuthenticationException, NetMikoTimeoutException) as e:
                print(e)
    return t_futures

# don't run on import
if __name__ == "__main__":
    data = {
        'tun_num': None,
        'wan_ip_1': '10.111.111.11',
        'wan_ip_2': '10.111.111.3',
        'tun_ip_1': '10.0.1.1 255.255.255.252',
        'tun_ip_2': '10.0.1.2 255.255.255.252'
    }
    with open('devicess.yaml') as src:
        devices = yaml.safe_load(src)
    device1, device2 = devices
    t = configure_vpn(device1, device2, "templates/gre_ipsec_vpn_1.txt",
                  "templates/gre_ipsec_vpn_2.txt", data)
    for output in t:
        print(output)