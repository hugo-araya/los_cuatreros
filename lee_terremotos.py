ar = open('terr.txt')
linea = ar.readline()
while linea != '':
    linea = linea.rstrip('\n')
    lista = linea.split()
    fecha = lista[0]
    lista_fecha = fecha.split('/')
    year = lista_fecha[2]
    print(year)
    linea = ar.readline()