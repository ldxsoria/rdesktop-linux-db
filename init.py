import controller
from ServersDao import ServersDao
from Servers import Servers
import logging as log
import os

controller.createDB()
controller.createTable()

opcion = None
os.system('clear')
while opcion != 3:
    #Este sera el menu principal
    print('Opciones')
    print('1) Listar conexion')
    print('2) Agregar conexion')
    print('3) Actualzar conexion')
    print('4) Salir')
    opcion = int(input('Ingresa tu opción (1-3) > '))

    #Este sera el menu de -> Listar equipos
    if opcion == 1:

        os.system('clear')
        dic_equipos = {} #Creo un diccionario, para usar # como un identificador
        n = 0 # llave del diccionario
        print('Los equipos registrados hasta ahora son:')

        equipos = ServersDao.selecionar()
        for equipo in equipos:
            n += 1
            print(f'{n}. {equipo[0]}')
            dic_equipos[n] = equipo[0]

        opcion = int(input('Ingresa el número del equipo a conectar (0 para salir)> '))
        if opcion != 0:
            pass
        else:
            pass
        os.system('clear')

    elif opcion == 2:
        os.system('clear')
        name = input('Ingresa el nombre del equipo >')
        ip = input(f'Ingresa la IP de {name} >')
        username = input('Ingresa el usuario > ')
        password = input('Ingresa la constraseña >')
        newRegistro = Servers(name, ip, username, password)
        ServersDao.intertar(newRegistro)
        print('Servidor registrado')
        os.system('clear')
    elif opcion == 3:
        os.system('clear')
        name = input('Ingresa el nombre de la conexion a actualizar >')
        new_ip = input(f'Ingresa la IP de {name} >')
        new_username = input('Ingresa el usuario > ')
        new_password = input('Ingresa la constraseña >')
        registro = Servers(name,new_ip,new_username,new_password)
        ServersDao.actualizar(registro)
    elif opcion == 4:
        print('Fin')
    else:
        os.system('clear')
        print('>>>> INGRESA UNA OPCION VALIDA <<<<<<<')
        

