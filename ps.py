import psutil, time, os
from pprint import pprint
import subprocess

refresh = 1

#while True:
freq_proc = psutil.cpu_freq()
usage_proc = psutil.cpu_percent()
usage_disk = psutil.disk_usage('/')
if_addrs = psutil.net_if_addrs()
connect = psutil.net_connections()
if_stats = psutil.net_if_stats()
counters = psutil.net_io_counters()
#    os.system('cls')
print('Максимальная частота проца: '+str(freq_proc[2]), 'Текущая частота проца: '+str(freq_proc[0]))
print('Процент использования проца: '+str(usage_proc))
print('Процент использования диска: '+str(usage_disk[3]))
print('IP адреса на сетевухе: ')
nets = if_addrs['Ethernet']
for net in nets:
    if net[2]:
        print(net[1], net[2])
pprint('Net speed = ' + str(if_stats['Ethernet'][2]), width=120)

#    time.sleep(refresh)