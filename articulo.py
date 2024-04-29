nombre = input('Nombre del producto: ')
clave = input('Codigo del producto: ')
precio = int(input('Precio del producto: '))
if clave == '01':
	precio_final = precio - precio * 0.1
else:
	precio_final = precio - precio * 0.2
print('Precio final: ', precio_final)
