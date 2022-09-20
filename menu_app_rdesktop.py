from RemoteDesktop import RemoteDesktop
from Server import Server
import logging as log
import os

opcion = None
os.system('clear')
while opcion != 3:
    #Este sera el menu principal
    print('Opciones')
    print('1) Listar equipos')
    print('2) Configuraciones')
    print('3) Salir')
    opcion = int(input('Ingresa tu opción (1-3) > '))

    #Este sera el menu de -> Listar equipos
    if opcion == 1:

        os.system('clear')
        dic_equipos = {} #Creo un diccionario, para usar # como un identificador
        n = 0 # llave del diccionario
        print('Los equipos registrados hasta ahora son:')

        equipos = RemoteDesktop.selecionar()
        for equipo in equipos:
            n += 1
            print(f'{n}. {equipo[0]}')
            dic_equipos[n] = equipo[0]

        opcion = int(input('Ingresa el número del equipo a conectar (0 para salir)> '))
        if opcion != 0:
            pass
        else:
            pass
        

