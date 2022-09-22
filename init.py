import controller
from ServersDao import ServersDao
from Servers import Servers
from MenuAcatualizar import MenuAcatualizar as Etapa
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

def actualizar(data_actual):

    pregunta_ip = Etapa(1, 'la ip','la nueva ip', data_actual.ip)
    pregunta_username = Etapa(2, 'el usuario','el nuevo usuario', data_actual.username)
    pregunta_password = Etapa(3, 'la contraseña', 'la nueva contraseña', data_actual.password)
    tupla = (pregunta_ip, pregunta_username, pregunta_password)
    eleccion = 'ejecutar'

    etapa = 0

    
    for e in range(0,3):

        print(f'¿Deseas actualizar {tupla[etapa].pregunta1} > {tupla[etapa].respuesta} ?\n1. Sí\n2. No')
        #Actualizar IP?
        ip = int(input('> '))
        if ip == 1:
            tupla[etapa].respuesta = input(f'Ingresa {tupla[etapa].pregunta2} de >')
            print(tupla[etapa].respuesta)
            etapa += 1
        elif ip == 2:
            #new_ip = data_actual.ip
            #print(tupla[etapa])
            etapa += 1
        else:
            print('OPCION INCORRECTA')

    print(f'{tupla[0].respuesta}, {tupla[1].respuesta}, {tupla[2].respuesta}')

    #Almacena los cambios en un nuevo objeto "Servers"
    data_actualizada = Servers(data_actual.name, tupla[0].respuesta, tupla[1].respuesta, tupla[2].respuesta)
    #Realiza un execute para guardas los cambios
    ServersDao.actualizar(data_actualizada)
#FIN actualizar()


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

    #Menu 2 REGISTRAR
    elif opcion == 2:
        os.system('clear')
        print('Los equipos registrados hasta ahora son:')
        equipos_registrados()
        print('INGRESA "0" PARA REGRESAR AL MENU\nPresiona "ENTER" para continuar')
        sub_opcion = input('> ')
        if sub_opcion == '0':
            pass
        else:
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

            actualizar(data_actual)
            x = input('>')
        else:
            pass

    #SALIR DEL PROGRAMA
    elif opcion == 0:
        print('Bye')
        break
    else:
        os.system('clear')
        print('>>>> INGRESA UNA OPCION VALIDA <<<<<<<')
        
