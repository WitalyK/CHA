# -*- coding: utf-8 -*-
from sys import argv
try:
    ip_m = argv[1]
    #ip_m = input("Введите IP и Маску в формате: 10.1.1.0/24:")
    ip = ip_m.split('/')[0].split('.')
    mask = ip_m.split('/')[1]
    s = '1'*int(mask)+'0'*(32-int(mask))
    ipp = '{:<8}  {:<8}  {:<8}  {:<8}'
    ipp1 = '{:08b}  {:08b}  {:08b}  {:08b}'
    print('Network:')
    ip[3]=0
    print(ipp.format(ip[0],ip[1],ip[2],ip[3]))
    print(ipp1.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))
    print('Mask:')
    print('/'+mask)
    ipp1 = '{}  {}  {}  {}'
    s1=s[0:8]
    s2=s[8:16]
    s3=s[16:24]
    s4=s[24:]
    print(ipp.format(int(s1,2),int(s2,2),int(s3,2),int(s4,2)))
    print(ipp1.format(s1,s2,s3,s4))
except IndexError:
    print('Неверный аргумент')
