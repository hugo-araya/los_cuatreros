# Lee los 4 puntos que determinan un rectangulo

# Punto 1
x1 = int(input('Coordenada x del punto 1: '))
y1 = int(input('Coordenada y del punto 1: '))
# Punto 2
x2 = int(input('Coordenada x del punto 2: '))
y2 = int(input('Coordenada y del punto 2: '))
# Punto 3
x3 = int(input('Coordenada x del punto 3: '))
y3 = int(input('Coordenada y del punto 3: '))
# Punto 4
x4 = int(input('Coordenada x del punto 4: '))
y4 = int(input('Coordenada y del punto 4: '))

ok = True

if y1 != y2:
    ok = False
if y3 != y4:
    ok = False
if x1 != x4:
    ok = False
if x2 != x3:
    ok = False

if ok == True:
    print('ES un rectangulo')
else:
    print('NO es un rectangulo')