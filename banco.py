# Entero cap_inv
# Real p_interes, interes_calculado, saldo
p_interes = float(input('Interes: '))
cap_inv = int(input('Capital: '))
interes_calculado = cap_inv * (p_interes / 100)
if interes_calculado > 7000:
    saldo = cap_inv + interes_calculado
else:
    saldo = cap_inv
print('Saldo: ', saldo)
