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

def datos_by_name(sub_opcion):
    name = dic_equipos[sub_opcion] #Chat name
    server = Servers(name=name) #Created object
    return ServersDao.buscar(server)

def ejecutar_conexion(sub_opcion):
    remote_server_db = datos_by_name(sub_opcion) #busca
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
    print('3) Actualizar una conexion existente')
    print('4) Eliminar una conexion existente')
    print('0) Salir')
    opcion = int(input('Ingresa tu opción (0-4) > '))

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


    #Menu 3 ACTUALIZAR
    elif opcion == 3:
        os.system('clear')
        dic_equipos = equipos_registrados()
        sub_opcion = int(input('Ingresa el número de la conexcion a actualizar (0 para salir) > '))

        if sub_opcion != 0:
            #busca la info segun la opcion
            datos_sub_opcion = datos_by_name(sub_opcion)
            #Crea un objeto "Servers" con los datos recibidos
            data_actual = Servers(name=datos_sub_opcion[0],ip=datos_sub_opcion[1],username=datos_sub_opcion[2],password=datos_sub_opcion[3])
            
            #Actualizar IP?
            print(f'¿Deseas actualizar la ip > {data_actual.ip}?\n1. Sí\n2. No')
            ip = int(input('> '))
            if ip == 1:
                new_ip = input(f'Ingresa la nueva IP de >')
            elif ip == 2:
                new_ip = data_actual.ip
            else:
                os.system('clear')
                print('OPCCION INCORRECTA')

            #Actualizar USERNAME?
            print(f'¿Deseas actualizar el usuario > {data_actual.username}?\n1. Sí\n2. No')
            ip = int(input('> '))
            if ip == 1:
                new_username = input(f'Ingresa el nuevo usuario >')
            elif ip == 2:
                new_username = data_actual.username
            else:
                print('OPCCION INCORRECTA')

            #Actualizar PASSWORD?
            print(f'¿Deseas actualizar la contraseña de {new_username}?\n1. Sí\n2. No')
            ip = int(input('> '))
            if ip == 1:
                new_password = input(f'Ingresa la nueva contraseña >')
            elif ip == 2:
                new_password = data_actual.password
            else:
                print('OPCCION INCORRECTA')
            
            #Almacena los cambios en un nuevo objeto "Servers"
            data_actualizada = Servers(data_actual.name, new_ip, new_username,new_password)
            #Realiza un execute para guardas los cambios
            ServersDao.actualizar(data_actualizada)
        else:
            pass
    
    #SALIR DEL PROGRAMA
    elif opcion == 0:
        print('Bye')
        break
    else:
        os.system('clear')
        print('>>>> INGRESA UNA OPCION VALIDA <<<<<<<')
        
