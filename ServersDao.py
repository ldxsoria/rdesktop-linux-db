import os
import sqlite3
import pathlib
from Servers import Servers

class ServersDao:
    """Este path es para conectarme a la DB que se alamacena en el mismo
        directorio de la aplicacion
    """
    PATH = pathlib.Path(__file__).parent.resolve()

    _SELECIONAR = f'SELECT * FROM servers'
    _BUSCAR = 'SELECT * FROM servers WHERE name=?'
    _INSERTAR = 'INSERT INTO servers (name,ip,username,password) values (?,?,?,?)'
    _ACTUALIZAR = "UPDATE servers SET ip=?, username=?, password=? WHERE name=?"
    _ELIMINAR = "DELETE FROM servers WHERE name=?"

    _CONECTAR = 'rdesktop %s -u %s -p %s'

    @classmethod
    def selecionar(cls):
        conn = sqlite3.connect(f'{cls.PATH}/rdesktop.db')
        resultado = []
        cursor = conn.cursor()
        cursor.execute(cls._SELECIONAR)
        registros = cursor.fetchall()
        conn.commit()
        conn.close()
        return registros

    @classmethod
    def buscar(cls, servers):
        conn = sqlite3.connect(f'{cls.PATH}/rdesktop.db')
        cursor = conn.cursor()
        valores = (servers.name,)
        cursor.execute(cls._BUSCAR,valores)
        registro = cursor.fetchone()
        conn.commit()
        conn.close()
        return registro

    @classmethod
    def intertar(cls, servers):
        conn = sqlite3.connect(f'{cls.PATH}/rdesktop.db')
        cursor = conn.cursor()
        valores = (servers.name, servers.ip, servers.username, servers.password)
        cursor.execute(cls._INSERTAR,valores)
        conn.commit()
        conn.close()

    @classmethod
    def actualizar(cls,servers):
        conn = sqlite3.connect(f'{cls.PATH}/rdesktop.db')
        cursor = conn.cursor()
        valores = (servers.ip, servers.username, servers.password, servers.name)
        cursor.execute(cls._ACTUALIZAR,valores)
        conn.commit()
        conn.close()

    @classmethod
    def eliminar(cls,servers):
        conn = sqlite3.connect(f'{cls.PATH}/rdesktop.db')
        cursor = conn.cursor()
        valores = (servers.name,)
        cursor.execute(cls._ELIMINAR,valores)
        conn.commit()
        conn.close()

        
    @classmethod
    def conectar(cls, servers):
        valores = (servers.ip, servers.username, servers.password)
        ejecutar = (cls._CONECTAR %valores)
        os.system(ejecutar)

if __name__ == '__main__':
    server1 = Servers('q','192.6.31.46','temp','P@ssw0rd')
    #server2 = Servers('soporte','172.19.1.24','temp','P@ssw0rd')
    #print(server1)
    #conectar = RemoteDesktop.conectar(server1)
    #print(conectar)
    #registrar = RemoteDesktop.intertar(server2)
    #actualizar = ServersDao.actualizar(server1)
    #eliminar = ServersDao.eliminar(server1)
    #server3 = Servers(name='soporte')
    #x = ServersDao.buscar(server3)
    #print(x)