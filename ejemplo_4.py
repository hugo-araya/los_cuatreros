
numero=2
sumando=3
lista = []
while (numero <= 1800):
    lista.append(numero) # lista + [numero]
    numero = numero + sumando
    if (sumando == 3):
        sumando = 2
    else:
        sumando = 3
print(lista)
print(len(lista))