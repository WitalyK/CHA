import sqlite3
from sys import argv
from tabulate import tabulate


def check_arg(args):
    if len(args) > 3 or len(args) == 2:
        print('Пожалуйста, введите два или ноль аргументов')
        return False
    elif len(args) == 1:
        return 0, 0
    else:
        return args[1], args[2]


def get_data_from_dhcp_output(connection, args=None):
    query1 = 'select * from dhcp where active = 1'
    query2 = 'select * from dhcp where active = 0'
    if args:
        query = query1 + ' and {} = ?'.format(args[0])
        result1 = connection.execute(query, (args[1], ))
        query = query2 + ' and {} = ?'.format(args[0])
        result2 = connection.execute(query, (args[1], ))
    else:
        result1 = connection.execute(query1)
        result2 = connection.execute(query2)
    if result1:
        print('Активные записи\n')
        print(tabulate([row for row in result1]))
    if result2:
        print('\nНе активные записи\n')
        print(tabulate([row for row in result2]))


def get_data_from_dhcp(key_fields, connection, args):
    if args[0] == 0:
        print('В таблице dhcp такие записи:\n')
        get_data_from_dhcp_output(connection)
    else:
        if args[0] not in key_fields:
            print('Данный параметр не поддерживается.\n')
            print('Допустимые значения параметров: mac, ip, vlan, interface, switch, active')
        else:
            print('Информация об устройствах с такими параметрами: ' + args[0] + ' ' + args[1] + '\n')
            get_data_from_dhcp_output(connection, args)


# don't run on import
if __name__ == "__main__":
    if check_arg(argv):
        db_name = 'dhcp_snooping.db'
        keys = ['mac', 'ip', 'vlan', 'interface', 'switch', 'active']
        conn = sqlite3.connect(db_name)
        t = check_arg(argv)
        get_data_from_dhcp(keys, conn, t)
        conn.close()
