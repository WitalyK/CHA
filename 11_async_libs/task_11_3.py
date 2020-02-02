# -*- coding: utf-8 -*-
"""
Задание 11.3

Создать сопрограмму (coroutine) config_device_and_check. Сопрограмма
должна подключаться по SSH с помощью netdev к одному устройству,
переходить в режим enable, в конфигурационный режим, выполнять указанные команды,
а затем выходить из конфигурационного режима. После  настройки команд, функция
должна проверять, что они настроены корректно. Для проверки используется словарь (пояснение ниже).
Если проверка не прошла, должно генерироваться исключение ValueError с текстом на каком
устройстве не прошла проверка. Если проверка прошла, функция должна возвращать строку
с результатами выполнения команды.

Параметры функции:

* device - словарь с параметрами подключения к устройству
* config_commands - список команд или одна команда (строка), которые надо выполнить
* check - словарь, который указывает как проверить настройку команд config_commands. По умолчанию значение None.

Словарь, который передается в параметр check должен содержать две пары ключ-значение:
* command - команда, которая используется для проверки конфигурации
* search_line - какая строка должна присутствовать в выводе команды command

Запустить сопрограмму и проверить, что она работает корректно одним из устройств
в файле devices_netmiko.yaml и командами в списке commands.
Пример команд и словаря для проверки настройки есть в задании.

При необходимости, можно использовать функции из предыдущих заданий
и создавать дополнительные функции.

Для заданий в этом разделе нет тестов!
"""
import asyncio, yaml, netdev, re
from pprint import pprint


async def config_device_and_check(device, config_commands, check=None):
    if isinstance(config_commands, str): config_commands = [config_commands]
    print(f"Подключаюсь к {device['host']}")
    async with netdev.create(**device) as ssh:
        print(f'Отправляю команды на {device["host"]}')
        output = await ssh.send_config_set(config_commands)
        print(f'Получили данные от {device["host"]}:')
        pprint(output)
        if check:
            output = await ssh.send_command(check['command'])
            pprint(output)
            if re.search(check['search_line'], output):
                print("The hardware is configured correctly")
            else:
                print("The hardware is configured wrong")


async def main(*args, **kwargs):
    return await config_device_and_check(*args, **kwargs)


if __name__ == "__main__":
    commands = ['router ospf 55',
                'auto-cost reference-bandwidth 1000000',
                'network 0.0.0.0 255.255.255.255 area 0']

    check_ospf = {'command': 'sh ip ospf',
                  'search_line': 'Routing Process "ospf 55" with ID'}
    with open('devices_netmiko.yaml') as f:
        devices = yaml.safe_load(f)
    asyncio.run(main(devices[0], commands, check_ospf))
