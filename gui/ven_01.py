from tkinter import *
from tkinter import ttk
ventana = Tk()
etiqueta = ttk.Label(ventana, text="Hello World!")
etiqueta.grid(column=0, row=0)
boton = ttk.Button(ventana, text="Quit", command=ventana.destroy)
boton.grid(column=1, row=0)
print('Estoy imprimiendo')
ventana.mainloop()
