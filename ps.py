import psutil, time, os
from pprint import pprint


def convert_to_gbit(valu):
    return valu/1024./1024./1024.*8/refresh

def send_stat(value):
    print("%0.3f" % convert_to_gbit(value))

refresh = 7
old_value = 0

while True:
    freq_proc = psutil.cpu_freq()
    usage_proc = psutil.cpu_percent()
    usage_disk = psutil.disk_usage('/')
    if_addrs = psutil.net_if_addrs()
    connect = psutil.net_connections()
    if_stats = psutil.net_if_stats()
    counters = psutil.net_io_counters()
    os.system('cls')
    print('Максимальная частота проца: '+str(freq_proc[2]), 'Текущая частота проца: '+str(freq_proc[0]))
    print('Процент использования проца: '+str(usage_proc))
    print('Процент использования диска: '+str(usage_disk[3]))
    print('IP адреса на сетевухе: ')
    nets = if_addrs['Ethernet']
    for net in nets:
        if net[2]:
            print(net[1], net[2])
    pprint('Net speed = ' + str(if_stats['Ethernet'][2]), width=120)
    # Загрузка сетевого адаптера
    new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    if old_value:
        send_stat(new_value - old_value)
    old_value = new_value
    time.sleep(refresh)

# Прием и отправка по сокету
#
# # Save as server.py
# # Message Receiver
# import os
# from socket import *
# host = ""
# port = 13000
# buf = 1024
# addr = (host, port)
# UDPSock = socket(AF_INET, SOCK_DGRAM)
# UDPSock.bind(addr)
# print "Waiting to receive messages..."
# while True:
#     (data, addr) = UDPSock.recvfrom(buf)
#     print "Received message: " + data
#     if data == "exit":
#         break
# UDPSock.close()
# os._exit(0)
#
# # Save as client.py
# # Message Sender
# import os
# from socket import *
# host = "127.0.0.1" # set to IP address of target computer
# port = 13000
# addr = (host, port)
# UDPSock = socket(AF_INET, SOCK_DGRAM)
# while True:
#     data = raw_input("Enter message to send or type 'exit': ")
#     UDPSock.sendto(data, addr)
#     if data == "exit":
#         break
# UDPSock.close()
# os._exit(0)