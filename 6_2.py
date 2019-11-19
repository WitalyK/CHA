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
flag = True
while flag:
    ip = input('Input IP Address: ')
    flag = False
    ipp = ip.split('.')
    if len(ipp) == 4:
        for i in ipp:
            if not i.isdigit():
                flag = True
                break
            if not (0 <= int(i) <= 255):
                flag = True
                break
        if not flag:
            ip1 = int(ip.split('.')[0])
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
        flag = True
    if flag:
        print('Неправильный IP-адрес!')

