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

import netdev
import itertools
from functools import wraps


async def check_and_cancel(task1, task2):
    while True:
        if task2.done():
            task1.cancel()
            return
        await asyncio.sleep(0.1)


def spinner(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        task1 = asyncio.create_task(spin())
        task2 = asyncio.create_task(func(*args, **kwargs))
        task3 = asyncio.create_task(check_and_cancel(task1, task2))
        #result = await func(*args, **kwargs)
        #task1.cancel()
        await task3
        result = await task2
        return result
        #return task2.result()
    return wrapper


async def spin():
    spinnerr = itertools.cycle('\|/-')
    while True:
        try:
            print(f'\r{next(spinnerr)} Waiting...', end='')
            await asyncio.sleep(0.3)
        except asyncio.exceptions.CancelledError:
            return


@spinner
async def connect_ssh(device, command):
    print(f"\nПодключаюсь к {device['host']}")
    try:
        async with netdev.create(**device) as ssh:
            return await ssh.send_command(command)
    except netdev.exceptions.TimeoutError:
        print('Connection error')


device_params = {'host': '10.111.111.11',
                 'username': 'admin',
                 'password': 'cisco',
                 'device_type': 'cisco_ios',
                 'secret': 'cisco'}


if __name__ == "__main__":
    print(asyncio.run(connect_ssh(device_params, 'sh clock')))

