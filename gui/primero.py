

if __name__ == "__main__":
    ar = open("datos.txt")
    linea = ar.readline()
    linea = linea.rstrip("\n")
    lista = linea.split(",")
    print(lista)
    print(len(lista))
    hab = float(lista[4])
    conta = float(lista[-2])
    print(hab, conta)
    tasa = conta/hab*100000
    print(tasa)













        


