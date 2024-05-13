import mibib as mia

def funcion1():
    # No recibi ni retorna
    print('Hola mundo desde nada')

def funcion2(x):
    y = 2 * x + 1
    return y

def funcion3():
    pass

if __name__ == '__main__':
    # mia.limpiar()
    valor = funcion2(3)
    print(valor)

