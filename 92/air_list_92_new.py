# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from re import finditer

d_corr = False
zag = '''wait operator 0 * * * * *

wait operator 0 

'''
while not d_corr:
    d = input('Введите дату необходимого отработанного плейлиста в формате ДД.ММ.ГГГГ:')
    dd = [num for num in d.split('.') if num.isdigit()]
    if len(dd)==3:
        if len(dd[2])==4 and len(dd[1])==2 and len(dd[0])==2:
            try:
                d1 = datetime(int(dd[2]), int(dd[1]), int(dd[0]))  + timedelta(days=1)
                d1 = "{:%d:%m:%Y}".format(d1)
                d_corr = True
            except ValueError:
                d_corr = False

airlog = 'air1_'+d1[6:]+d1[3:5]+d1[0:2]+'.log'

try:
    with open(airlog) as log1, open('otrabot_za_'+dd[0]+'_'+dd[1]+'_'+dd[2]+'_92.air', 'w') as air:
        regex = (r'\d{2}:\d{2}:\d{2}\.\d{2} (?:Script take:|Script skip:).+ \[ (.+) \]')
        air.write(zag)
        nec_log = finditer(regex, log1.read())
        for match in nec_log:
            air.write(match.group(1)+'\n')

except FileNotFoundError:
    print('Необходим файл: '+airlog)
    input('Нажмите ENTER и прощайте.')


#02:00:00.01 Script take: 0 4 [ movie 00:13:54.32 Z:\OnAir\11_19\-3 Вочакыв Виктория Агаркова 19 11 19.m2t ]
#02:13:54.33 Script skip: 0 5 [ comment 0 Рекламный блок 55 начало - 02:13 ]
