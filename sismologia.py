import matplotlib.pyplot as plt

def lee_datos(nombre):
    datos = []
    ent = open(nombre)
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split()
        datos.append(lista)
    ent.close()
    return datos

def funcion_a(datos):
    mayor = -1
    for lista in datos:
        if float(lista[4]) > mayor:
            mayor = float(lista[4])
            fecha = lista[0]
            hora = lista[1]
    return [fecha, hora, mayor]

def funcion_b(datos):
    contador = 0
    for lista in datos:
        if float(lista[4]) >= 7 and float(lista[4]) < 8:
            contador = contador + 1
    return contador

def funcion_c(datos):
    contador = 0
    for lista in datos:
        if float(lista[4]) >= 8 and float(lista[4]) < 9:
            contador = contador + 1
    return contador

def funcion_d(datos):
    contador = 0
    for lista in datos:
        if float(lista[4]) >= 9:
            contador = contador + 1
    return contador

def funcion_e(datos):
    contador = 0
    for lista in datos:
        fecha = lista[0]
        fecha = fecha.split('/')
        if int(fecha[2]) < 1600:
            contador = contador + 1
    return contador

def funcion_f(datos):
    contador = 0
    for lista in datos:
        fecha = lista[0]
        fecha = fecha.split('/')
        if int(fecha[2]) >= 1600 and int(fecha[2]) < 1700:
            contador = contador + 1
    return contador 

def funcion_g(datos):
    contador = 0
    for lista in datos:
        fecha = lista[0]
        fecha = fecha.split('/')
        if int(fecha[2]) >= 1700 and int(fecha[2]) < 1800:
            contador = contador + 1
    return contador 

def muestra_datos(dato_a, dato_b, dato_c, dato_d, dato_e, dato_f, dato_g):
    print('Fecha:', dato_a[0], 'y hora:', dato_a[1], 'del mayor sismo registrado.')
    print()
    print('Cantidad de sismos >= 7.0 y < 8.0:', dato_b)
    print()
    print('Cantidad de sismos >= 8.0 y < 9.0:', dato_c)
    print()
    print('Cantidad de sismos >= 9.0:', dato_d)
    print()
    print('Cantidad de sismos >= 9.0:', dato_e)
    print()
    print('Cantidad de sismos >= 9.0:', dato_f)
    print()
    print('Cantidad de sismos >= 9.0:', dato_g)

def grafica(dato_e, dato_f, dato_g):
    x = [16, 17, 18]
    y = [dato_e, dato_f, dato_g]
    plt.bar(x, y)
    plt.show()

if __name__ == "__main__":
    datos = lee_datos('terr.txt')
    dato_a = funcion_a(datos)
    dato_b = funcion_b(datos)
    dato_c = funcion_c(datos)
    dato_d = funcion_d(datos)
    dato_e = funcion_e(datos)
    dato_f = funcion_f(datos)
    dato_g = funcion_g(datos)
    muestra_datos(dato_a, dato_b, dato_c, dato_d, dato_e, dato_f, dato_g)
    grafica(dato_e, dato_f, dato_g)

