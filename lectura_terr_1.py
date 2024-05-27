
terr_mes = []
mes_buscado = 1
while mes_buscado <=12:
    ar = open('terr.txt')
    cont = 0
    linea = ar.readline()
    while linea != '':
        linea = linea.rstrip('\n')
        lista = linea.split()
        fecha = lista[0]
        fecha1 = fecha.split('/')
        dia = fecha1[0]
        mes = fecha1[1]
        agno = fecha1[2]
        if int(mes) == mes_buscado:
            cont = cont + 1
        linea = ar.readline()
    terr_mes.append(cont)
    mes_buscado = mes_buscado + 1
    ar.close()

meses = ['Enero     ', 'Febrero   ', 'Marzo     ', 'Abril     ', 'Mayo      ', 'Junio     ', 'Julio     ', 'Agosto    ','Septiembre','Octubre   ','Noviembre ', 'Diciembre ']
i = 0
while i < 12:
    print(meses[i],' -> ',terr_mes[i])
    i = i + 1
    






