import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from tkinter import Menu

def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()

def funcion_acerca_de():
    mBox.showinfo(message="Creado por Hugo Araya Carrasco\nSeptiembre 2020", title="Acerca de")

ventana = tk.Tk()
ventana.title("Ejemplo Tkinter")
ventana.resizable(True, True)
barra_menu = Menu(ventana)
ventana.config(menu = barra_menu)

menu_archivo = Menu(barra_menu)
menu_archivo.add_command(label = "Nuevo")
menu_archivo.add_separator()
menu_archivo.add_command(label = "Salir", command = funcion_salir)
barra_menu.add_cascade(label = "Archivo", menu = menu_archivo)

menu_edit = Menu(barra_menu)
menu_edit.add_command(label = "undo")
menu_edit.add_command(label = "redo")
barra_menu.add_cascade(label = "Edit", menu = menu_edit)

menu_ayuda = Menu(barra_menu)
menu_ayuda.add_command(label = "Acerca de", command = funcion_acerca_de)
barra_menu.add_cascade(label = "Ayuda", menu=menu_ayuda)

ventana.mainloop()