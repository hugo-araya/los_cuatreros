SALTO = '\n'
ent = open('ejemplo.txt')
linea = ent.readline().rstrip('\n')
sal = open('salida.txt', 'w')
sal.write(linea+SALTO)
sal.write('Chao'+SALTO)
sal.close()