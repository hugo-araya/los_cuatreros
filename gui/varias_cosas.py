import tkinter as tk 
from tkinter import ttk

def validar(): 
    nombre = nombre_entry.get() 
    password = password_var.get() 
    print("El usuario es : " + nombre) 
    print("La password es : " + password) 
    nombre_var.set("") 
    password_var.set("") 

def analiza(caracter):
    print("analizando")
    print(caracter)

if __name__ == "__main__":
    root=tk.Tk() 
    root.geometry("600x400") 
    root.config(bg = 'beige')
    nombre_var = tk.StringVar() 
    password_var = tk.StringVar() 
    nombre_label = ttk.Label(root, text = 'Usuario', font = ('courier',14, 'bold'), background = 'red') 
    valida = root.register(analiza)
    nombre_entry = ttk.Entry(root, textvariable = nombre_var,font = ('calibre',14,'normal'), validate = 'key', validatecommand=(valida, '%S')) 

    password_label = ttk.Label(root, text = 'Password', font = ('courier',14,'bold')) 
    password_entry = ttk.Entry(root, textvariable = password_var, font = ('calibre',14,'normal'), show = '.') 
    validar_btn = ttk.Button(root,text = 'Validar', command = validar) 
    nombre_label.grid(row = 0, column = 0) 
    nombre_entry.grid(row = 0, column = 1) 
    password_label.grid(row = 1, column = 0) 
    password_entry.grid(row = 1, column = 1) 
    validar_btn.grid(row = 2, column = 1) 
    root.mainloop() 