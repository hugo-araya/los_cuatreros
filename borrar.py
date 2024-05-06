import os

sistema = os.name
if sistema == 'posix':
    os.system('clear')
else:
    os.system('cls')

nombre = 'juan perez soto'
print(len(nombre))
