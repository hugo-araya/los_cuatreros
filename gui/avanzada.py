import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from tkinter import *

def funcion1_click():
    boton1.configure(text = 'Me presionastes')
    etiqueta1.configure(foreground = 'red')

def funcion2_click():
    boton2.configure(text = "Hola " + nombre.get())

def funcion1_caja_mensaje():
    mBox.showinfo(message = 'Creado por Hugo Araya Carrasco\nOctubre 2020.', title = 'Mensaje 1')

def funcion2_caja_mensaje():
    respuesta = mBox.askyesno(message = 'Desea Continuar?', title = 'Mensaje 2')
    print(respuesta)

def funcion3_caja_mensaje():
    respuesta = mBox.askyesnocancel(message = 'Que hacemos?', title = 'Mensaje 3')
    if respuesta == True:
        print("Aprete yes")
    elif respuesta == False:
        print("Aprete no")
    else:
        print("Aprete Cancel")

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Programacion avanzada")
    ventana.resizable(True, True)
    ventana.geometry("500x300")
    ventana.configure(bg = 'beige')

    etiqueta1 = ttk.Label(ventana, text = "Hola Mundo")
    etiqueta1.grid(row = 1, column = 1)

    boton1 = ttk.Button(ventana, text = "Me presionas", command = funcion1_click)
    boton1.grid(row = 2, column = 2)

    etiqueta2 = ttk.Label(ventana, text = "Escribe tu nombre")
    etiqueta2.grid(row = 3, column = 1)

    nombre = tk.StringVar()
    preguntar_nombre = ttk.Entry(ventana, width = 20, textvariable = nombre)
    preguntar_nombre.grid(row = 3, column = 2)

    boton2 = ttk.Button(ventana, text = "Presiona aqui", command = funcion2_click)
    boton2.grid(row = 4, column = 2)

    boton3 = ttk.Button(ventana, text = "Mensaje 1", command = funcion1_caja_mensaje)
    boton3.grid(row = 5, column = 3)
    boton4 = ttk.Button(ventana, text = "Mensaje 2", command = funcion2_caja_mensaje)
    boton4.grid(row = 6, column = 3)
    boton5 = ttk.Button(ventana, text = "Mensaje 3", command = funcion3_caja_mensaje)
    boton5.grid(row = 7, column = 3)
    imagen = PhotoImage(file = 'otro.png')
    imagen_lbl = ttk.Label(ventana, image = imagen)
    imagen_lbl.grid(row = 8, column = 3)

    boton6 = ttk.Button(ventana, image = imagen)
    boton6.grid(row = 9, column = 3)
    boton3.focus()
    ventana.mainloop()


