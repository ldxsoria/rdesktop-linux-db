import sqlite3

conexion = sqlite3.connect('rdesktop.db')
try:
    conexion.execute("""
    
                        create table server(
                            name  text primary key,
                            ip text,
                            username text,
                            password text
                        )
                    """)

    print("Se creo la tabla server")
except sqlite3.OperationalError:
    print("La tabla server ya existe")
conexion.close()