# -*- coding: utf-8 -*-
"""
Задание 12.2

Создать сопрограмму (coroutine) ping_ip_addresses, которая проверяет
пингуются ли IP-адреса в списке.
Проверка IP-адресов должна выполняться параллельно (concurrent).

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:

* список доступных IP-адресов
* список недоступных IP-адресов


Для проверки доступности IP-адреса, используйте утилиту ping встроенную в ОС.

Запустить сопрограмму и проверить, что она работает корректно.
При необходимости можно создавать дополнительные функции.

Для заданий в этом разделе нет тестов!

"""
import asyncio, re
from pprint import pprint


async def ping(ip):
    regex = r'.+ TTL=.+'
    reply = await asyncio.create_subprocess_shell(
        f'ping -n 2 {ip}',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await reply.communicate()
    if re.findall(regex, stdout.decode('cp866')):
        return True, ip
    else:
        return False, ip


async def ping_ip_addresses(list_ip):
    awailable_ip = []
    unawailable_ip = []
    tasks = [asyncio.create_task(ping(ip)) for ip in list_ip]
    for future in asyncio.as_completed(tasks):
        result = await future
        if result[0]:
            awailable_ip.append(result[1])
        else:
            unawailable_ip.append(result[1])
    return awailable_ip, unawailable_ip


# don't run on import
if __name__ == "__main__":
    ip_list = ['192.168.0.1', '192.168.0.133', '192.168.0.157',
               '192.168.0.11', '192.168.0.234', '192.168.0.7',
               '192.168.0.6', '192.168.0.88', '192.168.11.11']
    pprint(asyncio.run(ping_ip_addresses(ip_list)), width=120)
