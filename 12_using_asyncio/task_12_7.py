# -*- coding: utf-8 -*-
"""
Задание 12.7


Создать сопрограмму (coroutine) spin. Сопрограмма должна работать бесконечно
и постоянно отображать spinner. Пример синхронного варианта функции показан ниже
и его можно взять за основу для асинхронного:

In [1]: import itertools
   ...: import time
   ...:
   ...: def spin():
   ...:     spinner = itertools.cycle('\|/-')
   ...:     while True:
   ...:         print(f'\r{next(spinner)} Waiting...', end='')
   ...:         time.sleep(0.1)
   ...:

In [3]: spin()
/ Waiting...
...
KeyboardInterrupt:

In [4]:

Создать декоратор для сопрограмм spinner, который запускает сопрограмму spin на время работы
декорируемой функции и останавливает его, как только функция закончила работу.
Проверить работу декоратора на сопрограмме connect_ssh.

Чтобы показать работу декоратора, записано видео с запуском декорированной функции:
https://youtu.be/YdeUxrlbAwk

Подсказка: задачи (task) можно отменять методом cancel.

При необходимости, можно использовать функции из предыдущих заданий
и создавать дополнительные функции.

Для заданий в этом разделе нет тестов!
"""
import asyncio
from asyncio.tasks import Task
from typing import Any

import netdev
import itertools
import time
from functools import wraps


def spinner(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        task = await spin()
        # await task
        result = await func(*args, **kwargs)
        # task.cancel()
        return result
    return wrapper


async def sp(spiner):
    while True:
        yield next(spiner)


async def spin():
    async for sp in spin1():
        # print(f'\r{sp} Waiting...', end='')
        return sp


async def spin1():
    spinnerr = itertools.cycle('\|/-')
    while True:
        yield next(spinnerr)
        # yield print(f'\r{next(spinnerr)} Waiting...', end='')
        time.sleep(0.1)


@spinner
async def connect_ssh(device, command):
    await asyncio.sleep(2)
    print(f"\nПодключаюсь к {device['host']}")
    try:
        async with netdev.create(**device) as ssh:
            output = await ssh.send_command(command)
            await asyncio.sleep(2)
            print(f'\nПолучили данные от {device["host"]}')
        return output
    except netdev.exceptions.TimeoutError:
        await asyncio.sleep(2)
        print('Connection error')
        return None


device_params = {'host': '10.111.111.11',
                 'username': 'admin',
                 'password': 'cisco',
                 'device_type': 'cisco_ios',
                 'secret': 'cisco'}


if __name__ == "__main__":
    print(asyncio.run(connect_ssh(device_params, 'sh clock')))

