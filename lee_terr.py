ent = open('terr.txt')
mayor = -1
for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split()
    magnitud = float(lista[4])
    if magnitud > mayor:
        mayor = magnitud
print(mayor)
ent.close()

