import os
import sqlite3
from Server import Server

class RemoteDesktop:
    _DB = sqlite3.connect("rdesktop.db")

    _SELECIONAR = "SELECT * FROM server"
    _INSERTAR = 'INSERT INTO server (name,ip,username,password) values (?,?,?,?)'
    _ACTUALIZAR = ""
    _ELIMINAR = ""
    _CONECTAR = 'rdesktop %s -u %s -p %s'

    @classmethod
    def selecionar(cls):
        return cls._DB.execute(cls._SELECIONAR)
        cls._DB.close()

    @classmethod
    def intertar(cls, server):
        valores = (server._name, server._ip, server._username, server._password)
        cls._DB.execute(cls._INSERTAR,valores)
        #sentencia = f'{cls._INSERTAR}, {valores}'
       # print(f'{sentencia}')
        #return cls._DB.execute(sentencia)
        cls._DB.close()
        


    @classmethod
    def conectar(cls, server):
        valores = (server._ip, server._username, server._password)
        ejecutar = (cls._CONECTAR %valores)
        os.system(ejecutar)

if __name__ == '__main__':
    server1 = Server('wten','192.6.31.46','soporte@maristas.local','C0mpaq')
    #print(server1)
    #conectar = RemoteDesktop.conectar(server1)
    #print(conectar)
    registrar = RemoteDesktop.intertar(server1)
    
    conexion=sqlite3.connect('rdesktop.db')
    
    cursor=conexion.execute('select * from server')
    for fila in cursor:
        print(fila)
    conexion.close()
    
