from os import path
from glob import glob
from yaml import safe_load
import sqlite3
from re import match


def add_data_switches(yaml_of_switches, connection):
    print('Добавляю данные в таблицу switches...')
    with open(yaml_of_switches) as f:
        templ = safe_load(f)
    query = 'INSERT into switches values (?, ?)'
    for values in templ.values():
        for t in values.items():
            try:
                with connection:
                    connection.execute(query, t)
            except sqlite3.IntegrityError as e:
                print('При добавлении данных: '+str(t)+' Возникла ошибка: ', e)


def add_data_dhcp(command_file_list, connection):
    print('Добавляю данные в таблицу dhcp...')
    regex = (r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    query = 'INSERT into dhcp values (?, ?, ?, ?, ?)'
    for command_file in command_file_list:
        sw = command_file.split('_')[0]
        with open(command_file) as f:
            for line in f:
                mat = match(regex, line)
                if mat:
                    try:
                        with connection:
                            connection.execute(query, mat.groups()+(sw,))
                    except sqlite3.IntegrityError as e:
                        print('При добавлении данных: '+str(mat.groups()+(sw,))+' Возникла ошибка: ', e)


#don't run on import
if __name__ == "__main__":
    db_name = 'dhcp_snooping.db'
    data_sw = 'switches.yml'
    dhcp_snoop_list = glob('sw?_dhcp*')
    is_db = path.exists(db_name)
    if is_db:
        conn = sqlite3.connect(db_name)
        add_data_switches(data_sw, conn)
        add_data_dhcp(dhcp_snoop_list, conn)
    else:
        print('База данных '+db_name+' не существует. Перед добавлением данных, ее надо создать')
