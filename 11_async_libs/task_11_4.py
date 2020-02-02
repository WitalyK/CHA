# -*- coding: utf-8 -*-
"""
Задание 11.4

Создать сопрограмму (coroutine) configure_network_device. Сопрограмма
должна подключаться по SSH к одному устройству, переходить в режим enable,
в конфигурационный режим, выполнять указанные команды, а затем выходить
из конфигурационного режима.

Для подключения должен функция должна использовать модуль netdev,
если device_type есть среди поддерживаемых платформ в netdev
и использовать asyncssh, если его среди платформ нет.
Для проверки второй ситуации можно прямо внутри функции удалить cisco_ios из устройств.

Параметры функции:

* device - словарь с параметрами подключения к устройству
* config_commands - список команд или одна команда (строка), которые надо выполнить

Функция возвращает строку с результатами выполнения команд (как в 11.1).

Как получить платформы netdev:

In [3]: netdev.platforms
Out[3]:
['arista_eos',
 'aruba_aos_6',
 'aruba_aos_8',
 'cisco_asa',
 'cisco_ios',
 'cisco_ios_xe',
 'cisco_ios_xr',
 'cisco_nxos',
 'fujitsu_switch',
 'hp_comware',
 'hp_comware_limited',
 'hw1000',
 'juniper_junos',
 'mikrotik_routeros',
 'terminal',
 'ubiquity_edge']

Запустить сопрограмму и проверить, что она работает корректно одним из устройств
в файле devices_netmiko.yaml и командами в списке commands.

При необходимости, можно использовать функции из предыдущих заданий
и создавать дополнительные функции.
Для заданий в этом разделе нет тестов!

"""
import asyncio, yaml, netdev
from task_11_3 import config_device_and_check
from task_11_1 import send_config_commands
from pprint import pprint


async def configure_network_device(device, config_commands):
    netdev_platforms = netdev.platforms
    if device['device_type'] in netdev_platforms:
        await config_device_and_check(device, config_commands)
    else:
        del device['device_type']
        del device['secret']
        result = await send_config_commands(device, config_commands)
        pprint(result)


if __name__ == "__main__":
    commands = ['router ospf 55',
                'auto-cost reference-bandwidth 1000000',
                'network 0.0.0.0 255.255.255.255 area 0']
    with open('devices_netmiko.yaml') as f:
        devices = yaml.safe_load(f)
    asyncio.run(configure_network_device(devices[0], commands))
