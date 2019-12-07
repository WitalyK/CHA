# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from shutil import copy
from re import match, findall

def find_rek_in_live(str_file, start_find):
    regex1 = (r'\n'+start_find+r':.+\[ movie.+\]\n(\d{2}:\d{2}:\d{2})(?:.+\[ movie.+ \]\n)+(\d{2}:\d{2}:\d{2}).+\[ movie.+ \]')
    if findall(regex1, str_file):
        time_span = findall(regex1, str_file)[0]
        ss = str_file.split('\n')
        r_strings = []
        flag = False
        for line in ss:
            if line.startswith(time_span[1]):
                break
            if line.startswith(time_span[0]):
                flag = True
            if flag:
                r_strings.append(match(r'\d{2}:\d{2}:.+\[ (.+) \]', line).group(1))
        len_rek = datetime.strptime(time_span[1], "%H:%M:%S") - datetime.strptime(time_span[0], "%H:%M:%S")
        return time_span[0], len_rek, r_strings
    else:
        return False


d_corr = False
zag = '''wait operator 0 * * * * *

wait operator 0 
comment 0 Начало эфира {}_91

'''
print('Необходимо обеспечить доступ к папкам \\\\192.168.0.91\D$\ForwarData\\ и \\\\192.168.0.99\D$\Журналы\\')
print('из этих папок будут копироваться журналы работы форвардов.')
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
    copy('\\\\192.168.0.99\D$\Журналы\\'+airlog1, airlog1+'1')
    copy('\\\\192.168.0.91\D$\ForwarData\\'+airlog1, airlog1)
    copy('\\\\192.168.0.91\D$\ForwarData\\'+airlog2, airlog2)
    with open(airlog1+'1') as dop:
        str_from_dop = dop.read()
    with open(airlog1) as log1, open(airlog2) as log2, open('otrabot_za_'+dd[0]+'_'+dd[1]+'_'+dd[2]+'_91.air', 'w') as air:
        air.write(zag.format(d))
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
                            end_live = datetime.strptime(s[0][0:8], "%H:%M:%S")
                            if is_rek:
                                start_rek = datetime.strptime(is_rek[0], "%H:%M:%S")
                                time_live1 = start_rek - start_live
                                live_time_list[0] = live_time_list[0].replace('video1 0', 'video1 0' + str(time_live1)+'.00')
                                live_time_list.insert(1, 'wait operator 0\n')
                                live_time_list.insert(2, 'comment 0 Рекламный блок w начало - ' + is_rek[0]+'\n')
                                i = 3
                                for li in is_rek[2]:
                                    live_time_list.insert(i, li+'\n')
                                    i += 1
                                live_time_list.insert(i, 'comment 0 Рекламный блок w конец\n')
                                time_live2 = end_live - (start_rek + is_rek[1])
                                live_time_list.insert(i+1, 'video1 0'+str(time_live2)+'.00'+live_time_list[0][18:]+'\n')
                            else:
                                time_live = end_live - start_live
                                live_time_list[0] = live_time_list[0].replace('video1 0', 'video1 0' + str(time_live)+'.00')
                            air.writelines(live_time_list)
                            live_time_list = []
                    if 'video1' in s[1]:
                        is_rek = find_rek_in_live(str_from_dop, s[0][0:2])
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
    print('Нет доступа к файлам: '+airlog1+' и '+airlog2+' на серверах 192.168.0.91 и 192.168.0.99')
    input('Нажмите ENTER и прощайте.')



