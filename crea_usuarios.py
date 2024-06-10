def lectura_datos(entrada):
   nombres = []
   ent = open(entrada)
   for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split()
    nombres.append(lista)
   ent.close()
   return nombres
   
def generador_usuarios(nombres):
   login = []
   for lista in nombres:
      username = (lista[0][0] + lista[1]).lower()
      if username in login:
         username = username + lista[2].upper()
      login.append(username)
   return login

def grabacion_usuarios(salida, login):
   sal = open(salida, 'w')
   for user in login:
      sal.write(user + '\n')
   sal.close()

if __name__ == "__main__": 
   nombres = lectura_datos("nombres_mios.txt") 
   login = generador_usuarios(nombres)
   grabacion_usuarios("usuarios_mios.txt", login) 