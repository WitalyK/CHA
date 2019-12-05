# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import re

d_corr = False
zag = '''wait operator 0 * * * * *

wait operator 0 
comment 0 Начало эфира {}_91

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

airlog1 = 'air1_'+dd[2]+dd[1]+dd[0]+'.log'
airlog2 = 'air1_'+d1[6:]+d1[3:5]+d1[0:2]+'.log'

try:
    with open(airlog1) as log1, open(airlog2) as log2, open('otrabot_za_'+dd[0]+'_'+dd[1]+'_'+dd[2]+'_91.air', 'w') as air:
        air.write(zag.format(d))
        flag = True
        rec = True
        live_time_list = []
        regex = (r'(?:\d{2}:\d{2}:\d{2}\.\d{2} (?:Script take:|Script skip:)|Skip:).+ \[ (.+) \]')
        for line in log1:
            match = re.match(regex, line)
            if match:
                if flag:
                    if line.startswith('05:59:'):
                        air.write(match.group(1) + '\n')
                        flag = False
                else:
                    if not rec:
                        if 'movie' not in match.group(1):
                            live_time_list.append(match.group(1) + '\n')
                        else:
                            rec = True
                            time_live = datetime.strptime(line[0:8], "%H:%M:%S") - start_live
                            live_time_list[0] = live_time_list[0].replace('video1 0', 'video1 0' + str(time_live)+'.00')
                            air.writelines(live_time_list)
                            live_time_list = []
                    if 'video1' in match.group(1):
                        start_live = datetime.strptime(line[0:8], "%H:%M:%S")
                        live_time_list.append(match.group(1) + '\n')
                        rec = False
                    if rec:
                        air.write(match.group(1) + '\n')

        for line in log2:
            if line.startswith('02:0'):
                break
            else:
                match = re.match(regex, line)
                if match:
                    air.write(match.group(1) + '\n')
except FileNotFoundError:
    print('Необходимы файлы: '+airlog1+' и '+airlog2)
    input('Нажмите ENTER и прощайте.')



