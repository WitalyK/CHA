# -*- coding: utf-8 -*-

'''
Задание 6.2a
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.
Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_not_correct = True
while ip_not_correct:
    ip = input('Input IP Address: ')
    ip_not_correct = False
    ipp = [num for num in [num for num in ip.split('.') if num.isdigit()] if (0 <= int(num) <= 255)]
    if len(ipp) == 4:
        ip1 = int(ipp[0])
        if 1 <= ip1 <= 223:
            print('unicast')
        elif 224 <= ip1 <= 239:
            print('multicast')
        elif ip == '255.255.255.255':
            print('local broadcast')
        elif ip == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
    else:
        ip_not_correct = True
        print('Неправильный IP-адрес!')

