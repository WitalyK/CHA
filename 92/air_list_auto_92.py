# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

d_corr = False
zag = '''wait operator 0 * * * * *

wait operator 0 

'''
d = datetime.now()
d1 = d - timedelta(days=1)
d = "{:%d:%m:%Y}".format(d)
d1 = "{:%d:%m:%Y}".format(d1)

airlog = 'air1_'+d[6:]+d[3:5]+d[0:2]+'.log'

try:
    with open(airlog) as log1, open('otrabot_za_'+d1[6:]+'_'+d1[3:5]+'_'+d1[0:2]+'_92.air', 'w') as air:
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



