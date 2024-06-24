import hemo
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox as mBox

def funcion_radio():
    print(opcion.get())

def funcion_analizar():
    if opcion.get() == 1:
        op = True
    else:
        op = False
    
    if opcion_gen.get() == 1:
        op_g = '0'
    else:
        op_g = '1'
    
    hem = float(var_hemo.get())
    ed = int(var_edad.get())
    datos = [hem, ed, op, op_g]
    resultado = hemo.analisis(datos)
    print(resultado)
    mBox.showinfo("Resultado analisis", resultado)


if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title('Analisis de Hemoglobina')
    ventana.geometry('400x400')
    lbl_hemo = ttk.Label(ventana, text = 'Hemoglobina')
    lbl_hemo.grid(column = 0, row = 0)

    var_hemo = tk.StringVar()
    btn_hemo = ttk.Entry(ventana,textvariable=var_hemo )
    btn_hemo.grid(column = 1, row = 0)
    
    lbl_edad = ttk.Label(ventana, text = 'Edad')
    lbl_edad.grid(column = 0, row = 1)

    var_edad = tk.StringVar()
    btn_edad = ttk.Entry(ventana,textvariable=var_edad )
    btn_edad.grid(column = 1, row = 1)

    tipo1 = 'Meses'
    tipo2 = 'Agnos'
    opcion = tk.IntVar()
    radio1 = ttk.Radiobutton(ventana,text = tipo1, variable = opcion, value = 1, command = funcion_radio)
    radio1.grid(column = 2, row =1)
    radio1 = ttk.Radiobutton(ventana,text = tipo2, variable = opcion, value = 2, command = funcion_radio)
    radio1.grid(column = 2, row =2)

    lbl_genero = ttk.Label(ventana, text = 'genero')
    lbl_genero.grid(column = 0, row = 3)

    gen1 = 'Femenino'
    gen2 = 'Masculino'
    opcion_gen = tk.IntVar()
    radio1 = ttk.Radiobutton(ventana,text = gen1, variable = opcion_gen, value = 1, command = funcion_radio)
    radio1.grid(column = 1, row =3)
    radio1 = ttk.Radiobutton(ventana,text = gen2, variable = opcion_gen, value = 2, command = funcion_radio)
    radio1.grid(column = 1, row =4)

    btn_analizar = ttk.Button(ventana, text = 'Analizar', command = funcion_analizar)
    btn_analizar.grid (column = 2, row = 5)
    
    ventana.mainloop()
