import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Hola Mundo')
# ventana.geometry('400x400')
# ventana.resizable(0,0)
ttk.Label(ventana, text = 'Hola raton con cola').grid(column = 0, row = 0)

ventana.mainloop()