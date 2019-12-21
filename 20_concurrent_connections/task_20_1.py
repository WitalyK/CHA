# -*- coding: utf-8 -*-
'''
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.
'''
import yaml, subprocess, tabulate, logging, re
from concurrent.futures import ThreadPoolExecutor, as_completed


logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

def awailable_ping(ip):
    logging.info(' ==> Check address '+ip)
    regex = (r'.+ TTL=.+')
    result = subprocess.run(['ping', '-n', '2', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    logging.info(' <== Checked address '+ip)
    if re.findall(regex, result.stdout.decode('cp866')):
        return True, ip
    else:
        return False, ip


def ping_ip_addresses(ip_list, limit=2):
    awailable_ip = []
    unawailable_ip =[]
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [executor.submit(awailable_ping, ip) for ip in ip_list]
        for f in as_completed(futures):
            try:
                if f.result()[0]:
                    awailable_ip.append(f.result()[1])
                else:
                    unawailable_ip.append(f.result()[1])
            except:
                print('Error')
    awa_len = len(awailable_ip)
    unawa_len = len(unawailable_ip)
    if awa_len != unawa_len:
        if awa_len > unawa_len:
            [unawailable_ip.append('') for i in range(awa_len-unawa_len)]
        else:
            [awailable_ip.append('') for i in range(unawa_len-awa_len)]
    return awailable_ip, unawailable_ip


#don't run on import
if __name__ == '__main__':
    file_yaml = 'devicess.yaml'
    with open(file_yaml) as src:
        devs = yaml.safe_load(src)
    tup = ping_ip_addresses([dev['ip'] for dev in devs], 3)
    print(tabulate.tabulate(list(zip(tup[0], tup[1])), headers=['Reachable', 'Unreachable'], tablefmt='grid'))