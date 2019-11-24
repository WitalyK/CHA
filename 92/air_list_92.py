# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

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
        air.write(zag)
        flag = True
        for line in log1:
            if flag:
                if ' [ wait time' in line:
                    air.write(line.split('[ ')[1].strip().rstrip(']')+'\n')
                    flag = False
            else:
                if 'Flags take:' in line:
                    air.write(line.split()[3]+'\n')
                elif 'Script take:' in line or 'Script skip:' in line or 'Skip:' in line:
                    s = line.split('[ ')
                    if line.startswith('05:59') and 'video1' in s[1]:
                        air.write(s[1].strip().rstrip(']') + '\n')
                        break
                    else:
                        air.write(s[1].strip().rstrip(']')+'\n')
except FileNotFoundError:
    print('Необходим файл: '+airlog)
    input('Нажмите ENTER и прощайте.')



