from os import path
from sqlite3 import connect


def create_db(db_name, schema):
    is_db = path.exists(db_name)
    conn = connect(db_name)
    if is_db:
        print('База данных существует')
    else:
        print('Создаю базу данных '+db_name+'...')
        with open(schema) as f:
            conn.executescript(f.read())
        print('Done')
    conn.close()


#don't run on import
if __name__ == "__main__":
    name_db = 'dhcp_snooping.db'
    shema = 'dhcp_snooping_schema.sql'
    create_db(name_db, shema)