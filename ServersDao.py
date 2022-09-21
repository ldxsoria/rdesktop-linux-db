import os
import sqlite3
from Server import Server

class ServersDao:
    
    _SELECIONAR = f'SELECT * FROM servers'
    _INSERTAR = 'INSERT INTO servers (name,ip,username,password) values (?,?,?,?)'
    _ACTUALIZAR = ""
    _ELIMINAR = ""

    _CONECTAR = 'rdesktop %s -u %s -p %s'

    @classmethod
    def selecionar(cls):
        conn = sqlite3.connect("rdesktop.db")
        resultado = []
        cursor = conn.cursor()
        cursor.execute(cls._SELECIONAR)
        registros = cursor.fetchall()
        conn.commit()
        conn.close()
        return registros

    @classmethod
    def intertar(cls, server):
        conn = sqlite3.connect("rdesktop.db")
        cursor = conn.cursor()
        valores = (server.name, server.ip, server.username, server.password)
        cursor.execute(cls._INSERTAR,valores)
        conn.commit()
        conn.close()
        
    @classmethod
    def conectar(cls, server):
        valores = (server.ip, server.username, server.password)
        ejecutar = (cls._CONECTAR %valores)
        os.system(ejecutar)

if __name__ == '__main__':
    server1 = Server('wten','192.6.31.46','soporte@maristas.local','C0mpaq')
    server2 = Server('soporte','172.19.1.24','soporte@maristas.local','C0mpaq')
    #print(server1)
    #conectar = RemoteDesktop.conectar(server1)
    #print(conectar)
    #registrar = RemoteDesktop.intertar(server2)
    x = RemoteDesktop.selecionar()
    for i in x:
        print(i)
    RemoteDesktop.filtro_solo_pk()
    
