import os

print('Iniciando instalación de rdesktop-db-on-linux...')

#Primero creo el directorio donde se alojara la app
try:
    os.makedirs('~/.local/share/rdbol', exist_ok=True)

    print('Directorio creado con exito')
except Exception as e:
    print('Directorio existente...')

os.system('nautilus ~/.local/share/rdbol')
print('Copiando archivos...')
