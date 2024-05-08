# Lee los 4 puntos que determinan un rectangulo
punto = []
# Puntos
i = 0
while i < 4:
    x = int(input('Coordenada x del punto '+str(i+1)+': '))
    y = int(input('Coordenada y del punto '+str(i+1)+': '))
    punto.append([x,y])
    i = i + 1

ok = True

if punto[0][1] != punto[1][1]:
    ok = False
if punto[2][1] != punto[3][1]:
    ok = False
if punto[0][0] != punto[3][0]:
    ok = False
if punto[1][0] != punto[2][0]:
    ok = False

if ok == True:
    print('ES un rectangulo')
else:
    print('NO es un rectangulo')