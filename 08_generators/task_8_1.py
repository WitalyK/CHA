# -*- coding: utf-8 -*-
"""
Задание 8.1

Создать генератор get_ip_from_cfg, который ожидает как аргумент имя файла,
в котором находится конфигурация устройства и возвращает все IP-адреса,
которые настроены на интерфейсах.

Генератор должен обрабатывать конфигурацию и возвращать кортеж на каждой итерации:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например: ('10.0.1.1', '255.255.255.0')

Проверить работу генератора на примере файла config_r1.txt.

"""
import re


def get_ip_from_cfg(filename):
    regex = ' ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)'
    with open(filename) as f:
        for line in f:
            match = re.match(regex, line)
            if match:
                yield match.group(1), match.group(2)


# don't run on import
if __name__ == "__main__":
    for n in get_ip_from_cfg('config_r1.txt'):
        print(n)
