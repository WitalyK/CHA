# -*- coding: utf-8 -*-
"""
Задание 11.5

Создать сопрограмму (coroutine) configure_router. Сопрограмма подключается
по SSH (с помощью netdev) к устройству и выполняет перечень команд
в конфигурационном режиме на основании переданных аргументов.

При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка, должно
генерироваться исключение ValueError с информацией о том, какая ошибка возникла,
при выполнении какой команды и на каком устройстве, например:
Команда "logging" выполнилась с ошибкой "Incomplete command" на устройстве 192.168.100.1

Параметры функции:

* device - словарь с параметрами подключения к устройству
* config_commands - список команд или одна команда (строка), которые надо выполнить

Функция возвращает строку с результатами выполнения команды.

Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#a
% Ambiguous command:  "a"

Запустить сопрограмму и проверить, что она работает корректно одним из устройств
в файле devices_netmiko.yaml.

При необходимости, можно использовать функции из предыдущих заданий
и создавать дополнительные функции.

Для заданий в этом разделе нет тестов!
"""
import asyncio, yaml, netdev
from pprint import pprint


async def configure_router(device, config_commands):
    errors = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']
    if isinstance(config_commands, str): config_commands = [config_commands]
    print(f"Подключаюсь к {device['host']}")
    async with netdev.create(**device) as ssh:
        print(f'Отправляю команды на {device["host"]}')
        output = await ssh.send_command('conf t\n', strip_command=False, strip_prompt=False)
        for command in config_commands:
            res = await ssh.send_command(command, strip_command=False, strip_prompt=False)
            for error in errors:
                if error in res:
                    raise ValueError(f'Команда {command} выполнилась с ошибкой {error} на устройстве {device["host"]}')
            output += res
        output += await ssh.send_command('end\n', strip_command=False, strip_prompt=False)
        print(f'Получили данные от {device["host"]}:')
        return output


async def main(*args, **kwargs):
    return await configure_router(*args, **kwargs)


if __name__ == "__main__":
    # списки команд с ошибками и без:
    commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
    correct_commands = ['logging buffered 20010', 'ip http server']
    with open('devices_netmiko.yaml') as f:
        devices = yaml.safe_load(f)
    pprint(asyncio.run(main(devices[0], correct_commands)))
