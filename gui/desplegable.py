import tkinter as tk
from tkinter import ttk

def muestra(event):
    print(elegido.get())

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Ejemplo Desplegable")
    ventana.geometry("300x300")
    ventana.resizable(True, True)

    elegido = tk.StringVar()
    ejemplo_combobox = ttk.Combobox(ventana, width=12, textvariable=elegido)
    ejemplo_combobox['values'] = ["uno", "dos","tres","cuatro", "cinco"]
    ejemplo_combobox.grid(row=1, column=1)
    ejemplo_combobox.bind('<<ComboboxSelected>>',muestra)
    ejemplo_combobox.current(0)
    ventana.mainloop()