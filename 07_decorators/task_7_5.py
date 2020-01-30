# -*- coding: utf-8 -*-
"""
Задание 7.5

Создать декоратор count_calls, который считает сколько раз декорируемая функция была вызвана.
При вызове функции должно отображаться количество вызовов этой функции.

Пример работы декоратора:
In [11]: @count_calls
    ...: def f1():
    ...:     return True
    ...:

In [12]: @count_calls
    ...: def f2():
    ...:     return False
    ...:

In [14]: for _ in range(5):
    ...:     f1()
    ...:
Всего вызовов: 1
Всего вызовов: 2
Всего вызовов: 3
Всего вызовов: 4
Всего вызовов: 5

In [15]: for _ in range(5):
    ...:     f2()
    ...:
Всего вызовов: 1
Всего вызовов: 2
Всего вызовов: 3
Всего вызовов: 4
Всего вызовов: 5

In [16]: for _ in range(5):
    ...:     f1()
    ...:
Всего вызовов: 6
Всего вызовов: 7
Всего вызовов: 8
Всего вызовов: 9
Всего вызовов: 10
"""
from functools import wraps


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f'Всего вызовов: {wrapper.count}')
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


@count_calls
def f1():
    return True


@count_calls
def f2():
    return False


if __name__ == "__main__":
    for _ in range(5):
        f1()
    print('f1****************')
    for _ in range(5):
        f2()
    print('f2****************')
    for _ in range(5):
        f1()
    print('f1****************')

