import os

def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

