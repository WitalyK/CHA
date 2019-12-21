# -*- coding: utf-8 -*-
'''
Задание 20.2

Создать функцию send_show_command_to_devices, которая отправляет
одну и ту же команду show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
'''
import yaml, netmiko, logging
from concurrent.futures import ThreadPoolExecutor, as_completed


logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.basicConfig(format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


def send_show_command_to_device(device, command):
    ip = device['ip']
    logging.info('Connect to '+ip)
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    logging.info('Recived from '+ip)
    return result


def send_show_command_to_devices(devices, command, filename, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [executor.submit(send_show_command_to_device, device, command) for device in devices]
        for future in as_completed(futures):
            try:
                print(future.result())
            except (netmiko.ssh_exception.NetMikoAuthenticationException, netmiko.ssh_exception.NetMikoTimeoutException) as e:
                print(e)
        # with open(filename, 'w') as dst:
        #     for f in as_completed(futures):
        #         dst.write(f.result())


#don't run on import
if __name__ == '__main__':
    yaml_file = 'devicess.yaml'
    comand = 'sh ip int br'
    file_com = 'commands.txt'
    with open(yaml_file) as src:
        devicess = yaml.safe_load(src)
    send_show_command_to_devices(devicess, comand, file_com)
    # with open(file_com) as f:
    #     for line in f:
    #         print(line)
