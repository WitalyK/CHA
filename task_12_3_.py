# -*- coding: utf-8 -*-
'''
Задание 12.3
Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.
Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов
Результат работы функции - вывод на стандартный поток вывода таблицы вида:
Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9
Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.
Для этого задания нет тестов
'''
from task_12_1 import ping_ip_addresses
from task_12_2 import convert_ranges_to_ip_list
from tabulate import tabulate


#не запускать при импорте
if __name__ == "__main__":
    diapazon_list = []
    while True:
        ip_or_diapazon = input(': ')
        if ip_or_diapazon == ' ':
            break
        diapazon_list.append(ip_or_diapazon)
    tup = ping_ip_addresses(convert_ranges_to_ip_list(diapazon_list))

    print(tabulate(list(zip(tup[0], tup[1])), headers=['Reachable', 'Unreachable'], tablefmt='grid'))

