import tkinter as tk
from tkinter import ttk
import random

def funcion_click():
    colores = ['red','blue','black', 'yellow', 'green']
    numero = random.randint(0,5)
    accion.configure(text = '*** haz hecho click ***')
    etiqueta.configure(foreground= colores[numero])
    
if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title('Hola Mundo')
    ventana.geometry('400x400')
    # ventana.resizable(0,0)
    etiqueta = ttk.Label(ventana, text = 'Hola raton con cola')
    etiqueta.grid(column = 0, row = 0)

    accion = ttk.Button(ventana, text = 'Haz click aqui!', command = funcion_click)
    accion.grid(column = 1, row = 0)

    ventana.mainloop()