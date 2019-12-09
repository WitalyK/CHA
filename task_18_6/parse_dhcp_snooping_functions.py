import sqlite3
from os import path
from tabulate import tabulate
from yaml import safe_load
from re import match
from datetime import timedelta, datetime


def create_db(db_name, db_schema):
    is_db = path.exists(db_name)
    conn = sqlite3.connect(db_name)
    if is_db:
        print('База данных уже существует, операция отменяется.')
    else:
        print('Создаю базу данных '+db_name+'...')
        with open(db_schema) as f:
            conn.executescript(f.read())
        print('Done')
    conn.close()


def add_data_switches(db_file, yaml_of_switches):
    conn = sqlite3.connect(db_file)
    with open(yaml_of_switches[0]) as f:
        templ = safe_load(f)
    query = 'INSERT into switches values (?, ?)'
    for values in templ.values():
        for t in values.items():
            try:
                with conn:
                    conn.execute(query, t)
            except sqlite3.IntegrityError as e:
                print('При добавлении данных: ' + str(t) + ' Возникла ошибка: ', e)
    conn.close()


def add_data(db_file, command_file_list):
    conn = sqlite3.connect(db_file)
    week_ago = datetime.today().replace(microsecond=0) - timedelta(days=7)
    conn.execute('DELETE from dhcp where last_active < ?', (str(week_ago), ))
    conn.commit()
    regex = (r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    query = "REPLACE into dhcp values (?, ?, ?, ?, ?, ?, datetime('now'))"
    for command_file in command_file_list:
        with open(command_file) as f:
            if '\\' in command_file:
                command_file = command_file.split('\\')[1]
            sw = command_file.split('_')[0]
            conn.execute('UPDATE dhcp set active = 0 where switch = ?', (sw,))
            for line in f:
                mat = match(regex, line)
                if mat:
                    try:
                        with conn:
                            conn.execute(query, mat.groups() + (sw, 1))
                    except sqlite3.IntegrityError as e:
                        print('При добавлении данных: ' + str(mat.groups() + (sw, 1)) + ' Возникла ошибка: ', e)
    conn.close()


def get_data(db_file, key, value):
    conn = sqlite3.connect(db_file)
    query = 'select * from dhcp where active = 1 and {} = ?'.format(key)
    result1 = conn.execute(query, (value,))
    query = 'select * from dhcp where active = 0 and {} = ?'.format(key)
    result2 = conn.execute(query, (value,))
    if result1:
        print('\nАктивные записи\n')
        print(tabulate([row for row in result1]))
    if result2:
        print('\nНе активные записи\n')
        print(tabulate([row for row in result2]))
    conn.close()


def get_all_data(db_file):
    conn = sqlite3.connect(db_file)
    result1 = conn.execute('select * from dhcp where active = 1')
    result2 = conn.execute('select * from dhcp where active = 0')
    if result1:
        print('\nАктивные записи\n')
        print(tabulate([row for row in result1]))
    if result2:
        print('\nНе активные записи\n')
        print(tabulate([row for row in result2]))
    conn.close()


