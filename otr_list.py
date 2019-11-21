# -*- coding: utf-8 -*-
d_corr = False
while not d_corr:
    d = input('Введите дату необходимого отработанного плейлиста в формате ДД.ММ.ГГГГ:')
    dd = d.split('.')
    if len(dd)==3:
        if dd[0].isdigit() and dd[1].isdigit() and dd[2].isdigit():
            if len(dd[2])==4 and len(dd[1])==2 and len(dd[0])==2:
                d_corr = True

#air1_20191118.log
#air1_20191118.log
airlog1 = 'air1_'+dd[2]+dd[1]+dd[0]+'.log'
airlog2 = 'air1_'+dd[2]+dd[1]+str(int(dd[0])+1)+'.log'

with open(airlog1) as log1, open(airlog2) as log2, open('otrabot_za_'+dd[0]+'_'+dd[1]+'_'+dd[2]+'.air', 'w') as air:
    flag = True
    for line in log1:
        if flag:
            if line.startswith('05:59:'):
                if line.find('Script take:')>0 or line.find('Script skip:')>0:
                    s = line.split('[ ')
                    air.write(s[1].strip().rstrip(']')+'\n')
                flag = False
        else:
            if line.find('Flags take:')>0:
                s = line.split()
                air.write(s[3]+'\n')
            elif line.find('Script take:')>0 or line.find('Script skip:')>0 or line.find('Skip:')>=0:
                s = line.split('[ ')
                air.write(s[1].strip().rstrip(']')+'\n')

    for line in log2:
        if line.startswith('02:0'):
            break
        else:
            if line.find('Flags take:')>0:
                s = line.split()
                air.write(s[3]+'\n')
            elif line.find('Script take:')>0 or line.find('Script skip:')>0:
                s = line.split('[ ')
                air.write(s[1].strip().rstrip(']')+'\n')




