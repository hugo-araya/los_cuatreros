import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Hola Mundo')
# ventana.geometry('400x400')
# ventana.resizable(0,0)
etiqueta = ttk.Label(ventana, text = 'Hola raton con cola')
etiqueta.pack()
etiqueta1 = ttk.Label(ventana, text = 'Hola raton sin cola')
etiqueta1.pack()

ventana.mainloop()