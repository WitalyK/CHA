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

def get_data_from_dhcp(connection, key_fields, args):
    if args[0] == 0:
        print('В таблице dhcp такие записи:')
        print(tabulate([row for row in connection.execute('select * from dhcp')]))
    else:
        if args[0] not in key_fields:
            print('Данный параметр не поддерживается.')
            print('Допустимые значения параметров: mac, ip, vlan, interface, switch')
        else:
            print('Информация об устройствах с такими параметрами: ' + args[0] + ' ' + args[1])
            query = 'select * from dhcp where {} = ?'.format(args[0])
            print(tabulate([row for row in connection.execute(query, (args[1],))]))


#don't run on import
if __name__ == "__main__":
    if check_arg(argv):
        db_name = 'dhcp_snooping.db'
        keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
        conn = sqlite3.connect(db_name)
        t = check_arg(argv)
        get_data_from_dhcp(conn, keys, t)
        conn.close()
