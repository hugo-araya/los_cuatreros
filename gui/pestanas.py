import tkinter as tk
from tkinter import ttk

def muestra(event):
    print(elegido.get())

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Ejemplo Pestaña")
    ventana.geometry("300x300")
    ventana.resizable(True, True)
    cuaderno = ttk.Notebook(ventana)
    pestana1 = ttk.Frame(cuaderno)
    cuaderno.add(pestana1, text ='Pestana_1')
    cuaderno.pack(expand=1, fill='both')
    pestana2 = ttk.Frame(cuaderno)
    cuaderno.add(pestana2, text = 'Pestana_2')
    pestana3 = ttk.Frame(cuaderno)
    cuaderno.add(pestana3, text = 'Pestana_3')
    boton1 = ttk.Button(pestana1, text ="Boton 1")
    boton1.pack()
    boton2 = ttk.Button(pestana2, text ="Boton 2")
    boton2.grid(row=1, column = 1)
    boton3 = ttk.Button(pestana3, text ="Boton 3")
    boton3.grid(row=1, column = 1)
    
    ventana.mainloop()