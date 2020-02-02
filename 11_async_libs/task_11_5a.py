# -*- coding: utf-8 -*-
"""
Задание 11.5a

Создать сопрограмму (coroutine) log_device_configuration.
Сопрограмма log_device_configuration должна использовать configure_router
из задания 11.5 для настройки оборудования. Оборудование должно настраиваться
параллельно.

После настройки оборудования, log_device_configuration должна записывать
результаты в log-файл (все результаты записываются в один log-файл):
* если настройка прошла успешно, записать в файл строку "Успешно настроен 192.168.100.1",
  а затем записать результат, который вернула configure_router
* если настройка не прошла проверку, записать в файл строку
  "Не получилось настроить 192.168.100.1" и записать сообщение из исключения

Параметры функции log_device_configuration:

* log_file - имя файла, в который будут записываться сообщения (сообщения могут быть в любом порядке)
* devices - список словарей с параметрами подключения к устройствам
* device_commands_map - словарь в котором указано на какое устройство
  отправлять какие команды. Пример словаря - commands

Пример команд и словаря для проверки настройки есть в задании.

При необходимости, можно использовать функции из предыдущих заданий
и создавать дополнительные функции.

Для заданий в этом разделе нет тестов!
"""
import asyncio, yaml
from task_11_5 import configure_router


async def log_device_configuration(log_file, devices_for_logging, device_commands_map):
    with open(log_file, 'w', encoding='utf-8') as log:
        tasks = [asyncio.create_task(concur(device, device_commands_map[device['host']]))
                 for device in devices_for_logging]
        for task in asyncio.as_completed(tasks):
            result = await task
            log.write(result)


async def concur(dev, conf_commands):
    try:
        result = await configure_router(dev, conf_commands)
        mess = f'Успешно настроен {dev["host"]}\n{result}\n'
    except ValueError as e:
        mess = f'Не получилось настроить {dev["host"]}\n{e}\n'
    return mess

if __name__ == "__main__":
    ospf = ['router ospf 55',
            'auto-cost reference-bandwidth 1000000',
            'network 0.0.0.0 255.255.255.255 area 0']
    logging_with_error = 'logging 0255.255.1'
    logging_correct = 'logging buffered 20010'

    commands = {'10.111.11.2': logging_correct,
                '10.111.111.3': logging_correct,
                '10.111.111.4': logging_with_error,
                '10.111.111.11': ospf}
    with open('devices_netmiko.yaml') as f:
        devices = yaml.safe_load(f)
    asyncio.run(log_device_configuration('log.txt', devices, commands))
