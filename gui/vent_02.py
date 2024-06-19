from tkinter import *
from tkinter import ttk

def funcion_boton():
    boton2.configure(text=" --> Me apretastes <--"+" "+nombre.get())
    etiqueta.configure(foreground = 'red')

if __name__ == '__main__':
    # Inicializar la ventana
    ventana = Tk()
    ventana.title("Hola ventana al mundo")
    ventana.geometry('200x300+400+300')
    #ventana.config(width=400, height=300)
    ventana.resizable(0,0)

    # Agregar una etiqueta
    etiqueta = ttk.Label(ventana, text = 'Buenos dias mundo!!!')
    etiqueta.grid(column = 0, row = 0)

    # Agregar un boton
    boton1 = ttk.Button(ventana, text ="Presiona aqui!!!")
    boton1.grid(column = 0, row = 1)

    # Agregar un boton con accion
    boton2 = ttk.Button(ventana, text ="Apreta aqui!!!", command = funcion_boton)
    boton2.grid(column = 0, row = 2)

    # Agregar caja de texto
    nombre = StringVar()
    preguntar = ttk.Entry(ventana, width = 20, textvariable = nombre)
    preguntar.grid(column = 0, row = 3)

    # Activar la ventana
    ventana.mainloop()
