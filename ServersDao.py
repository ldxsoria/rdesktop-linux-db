import os
import sqlite3
from Servers import Servers

class ServersDao:
    
    _SELECIONAR = f'SELECT * FROM servers'
    _INSERTAR = 'INSERT INTO servers (name,ip,username,password) values (?,?,?,?)'
    _ACTUALIZAR = "UPDATE servers SET ip=?, username=?, password=? WHERE name=?"
    _ELIMINAR = "DELETE FROM servers WHERE name=?"

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
    def intertar(cls, servers):
        conn = sqlite3.connect("rdesktop.db")
        cursor = conn.cursor()
        valores = (server.name, server.ip, server.username, server.password)
        cursor.execute(cls._INSERTAR,valores)
        conn.commit()
        conn.close()

    @classmethod
    def actualizar(cls,servers):
        conn = sqlite3.connect('rdesktop.db')
        cursor = conn.cursor()
        valores = (servers.ip, servers.username, servers.password, servers.name)
        cursor.execute(cls._ACTUALIZAR,valores)
        conn.commit()
        conn.close()

    @classmethod
    def eliminar(cls,servers):
        conn = sqlite3.connect('rdesktop.db')
        cursor = conn.cursor()
        valores = (servers.name,)
        cursor.execute(cls._ELIMINAR,valores)
        conn.commit()
        conn.close()

        
    @classmethod
    def conectar(cls, servers):
        valores = (server.ip, server.username, server.password)
        ejecutar = (cls._CONECTAR %valores)
        os.system(ejecutar)

if __name__ == '__main__':
    server1 = Servers('q','192.6.31.46','soporte@maristas.local','C0mpaq')
    server2 = Servers('soporte','172.19.1.24','soporte@maristas.local','C0mpaq')
    #print(server1)
    #conectar = RemoteDesktop.conectar(server1)
    #print(conectar)
    #registrar = RemoteDesktop.intertar(server2)
    #actualizar = ServersDao.actualizar(server1)
    eliminar = ServersDao.eliminar(server1)