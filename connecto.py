import sqlite3 as sqlite3

def createDB():
    try:
        conn = sql.connect('rdesktop.db')
        conn.commit()
        conn.close()
    except:
        print('Base de datos ya exitente')

def createTable():
    try:
        conn = sql.connect('rdesktop.db')
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
    except:
        print('Tabla ya exitente')


if __name__ == '__main__':
    createDB()
    createTable()