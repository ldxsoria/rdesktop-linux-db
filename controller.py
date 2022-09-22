import sqlite3 as sql

def createDB(path):
    try:
        conn = sql.connect(f'{path}/rdesktop.db')
        conn.commit()
        conn.close()
        print('DB created')
    except:
        pass

def createTable(path):
    try:
        conn = sql.connect(f'{path}/rdesktop.db')
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE servers (
                name text primary key,
                ip text,
                username text,
                password text

            )"""
        )
        conn.commit()
        conn.close()
        print('Tabla creado con exito')
    except:
        print('Tabla ya exitente')


if __name__ == '__main__':
    #createDB('.')
    createTable('.')