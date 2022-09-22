import controller
from ServersDao import ServersDao
from Servers import Servers
import logging as log
import os
import pathlib

_PATH = ServersDao.PATH
#_PATH = pathlib.Path(__file__).parent.resolve()

controller.createDB(_PATH)
controller.createTable(_PATH)

def equipos_registrados():
    dic_registros = {} #Creo un diccionario, para usar # como un identificador
    n = 0 # llave del diccionario
    equipos = ServersDao.selecionar()
    for equipo in equipos:
        n += 1
        print(f'{n}. {equipo[0]}') #Imprimo la lista de objetos registrados con un numero correlativo
        dic_registros[n] = equipo[0] #Aqui
    return dic_registros


def ejecutar_conexion(opcion):
    name = dic_equipos[opcion] #Chat name
    server = Servers(name=name) #Created object
    remote_server_db = ServersDao.buscar(server) #Search object by name selected
    remote_server = Servers(ip=remote_server_db[1],username=remote_server_db[2], password=remote_server_db[3])
    remote_conn = ServersDao.conectar(remote_server)
    #print(remote_server)

opcion = None
while opcion != 4:
    #Este sera el menu principal
    os.system('clear')
    print('RDESKTOP DATABASE\nOpciones:')
    print('1) Conectarme a un equipo')
    print('2) Agregar una nueva conexion')
    print('3) Actualizar o eliminar conexiones existentes')
    print('4) Salir')
    opcion = int(input('Ingresa tu opción (1-3) > '))

    #Menu 1
    if opcion == 1:
        os.system('clear')
        print('Los equipos registrados hasta ahora son:')
        dic_equipos = equipos_registrados()
        sub_opcion = int(input('Ingresa el número del equipo a conectar (0 para salir) > '))
        if sub_opcion != 0:
            ejecutar_conexion(sub_opcion)
        else:
            pass

    #Menu 2
    elif opcion == 2:
        os.system('clear')
        print('Los equipos registrados hasta ahora son:')
        equipos_registrados()
        name = input('Ingresa el nombre del equipo >')
        ip = input(f'Ingresa la IP de {name} >')
        username = input('Ingresa el usuario > ')
        password = input('Ingresa la constraseña >')
        newRegistro = Servers(name, ip, username, password)
        ServersDao.intertar(newRegistro)
        print('Servidor registrado')


    #Menu 3
    elif opcion == 3:
        os.system('clear')
        equipos_registrados()
        sub_opcion = int(input('Ingresa el número de la conexcion a actualizar (0 para salir) > '))
        if sub_opcion != 0:

            new_ip = input(f'Ingresa la IP de {sub_opcion} >')
            new_username = input('Ingresa el usuario > ')
            new_password = input('Ingresa la constraseña >')
            registro = Servers(name,new_ip,new_username,new_password)
            ServersDao.actualizar(registro)
        else:
            pass

    elif opcion == 4:
        print('Bye')
        break
    else:
        os.system('clear')
        print('>>>> INGRESA UNA OPCION VALIDA <<<<<<<')
        
