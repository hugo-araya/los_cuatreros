# Entero cap_invertir
# Real ganancia
cap_invertir = int(input('Ingrese capital: '))
porcentaje = float(input('Indique el procentje: '))
ganancia = cap_invertir * porcentaje / 100
salida = 'Para una inversion de $'+str(cap_invertir)+' la ganancia es $'+str(ganancia)
print(salida)
