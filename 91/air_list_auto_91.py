# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

d_corr = False
zag = '''wait operator 0 * * * * *

wait operator 0 
comment 0 Начало эфира {}_91

'''
d = datetime.now()
d1 = d - timedelta(days=1)
d = "{:%d:%m:%Y}".format(d)
d1 = "{:%d:%m:%Y}".format(d1)

airlog1 = 'air1_'+d1[6:]+d1[3:5]+d1[0:2]+'.log'
airlog2 = 'air1_'+d[6:]+d[3:5]+d[0:2]+'.log'

try:
    with open(airlog1) as log1, open(airlog2) as log2, open('otrabot_za_'+d1[0:2]+'_'+d1[3:5]+'_'+d1[6:]+'_91.air', 'w') as air:
        air.write(zag.format(d1))
        flag = True
        rec = True
        live_time_list = []
        for line in log1:
            if flag:
                if line.startswith('05:59:'):
                    if 'Script take:' in line or 'Script skip:' in line:
                        air.write(line.split('[ ')[1].strip().rstrip(']')+'\n')
                    flag = False
            else:
                if 'Flags take:' in line:
                    air.write(line.split()[3]+'\n')
                elif 'Script take:' in line or 'Script skip:' in line or 'Skip:' in line:
                    s = line.split('[ ')
                    if not rec:
                        if 'movie' not in s[1]:
                            live_time_list.append(s[1].strip().rstrip(']') + '\n')
                        else:
                            rec = True
                            time_live = datetime.strptime(s[0][0:8], "%H:%M:%S") - start_live
                            live_time_list[0] = live_time_list[0].replace('video1 0', 'video1 0' + str(time_live)+'.00')
                            air.writelines(live_time_list)
                            live_time_list = []
                    if 'video1' in s[1]:
                        start_live = datetime.strptime(s[0][0:8], "%H:%M:%S")
                        live_time_list.append(s[1].strip().rstrip(']') + '\n')
                        rec = False
                    if rec:
                        air.write(s[1].strip().rstrip(']')+'\n')

        for line in log2:
            if line.startswith('02:0'):
                break
            else:
                if 'Flags take:' in line:
                    air.write(line.split()[3]+'\n')
                elif 'Script take:' in line or 'Script skip:' in line:
                    air.write(line.split('[ ')[1].strip().rstrip(']')+'\n')
except FileNotFoundError:
    print('Необходимы файлы: '+airlog1+' и '+airlog2)
    input('Нажмите ENTER и прощайте.')



