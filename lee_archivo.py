ent = open('ejemplo.txt')
for linea in ent:
    linea = linea.rstrip('\n')
    print(linea)
ent.close()
