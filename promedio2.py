
contador = 0
suma = 0
cantidad = int(input('Cantidad de notas: '))
while contador < cantidad:
    nota = float(input('Ingrese nota '+str(contador+1)+': '))
    if nota >=1 and nota <=7:
        suma = suma + nota
        contador = contador + 1
    else:
        print('Nota no valida, reingrese la nota:')
promedio = suma / cantidad
print('Promedio : ', promedio)
if promedio >= 4:
    print('Dios es grande, se salvo.')
else:
    print('R.I.P.')
    
