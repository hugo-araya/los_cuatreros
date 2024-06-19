from tkinter import * 

def mensaje():
    label3 = Label(ventana,text="Clave invalida") 
    label3.grid(row=4,column=2) 

ventana = Tk()
ventana.title('Ejemplo')
ventana.geometry("300x500")
label1 = Label(ventana,text="               0") 
label1.grid(row=1,column=1) 
boton7 = Button(ventana,text="7")
boton7.grid(row=3,column=1)
boton8 = Button(ventana,text="8")
boton8.grid(row=3,column=2)
boton9 = Button(ventana,text="9")
boton9.grid(row=3,column=3)
boton4 = Button(ventana,text="4")
boton4.grid(row=4,column=1)
boton5 = Button(ventana,text="5")
boton5.grid(row=4,column=2)
boton6 = Button(ventana,text="6")
boton6.grid(row=4,column=3)

variable_user = StringVar()
caja1 = Entry(ventana,textvariable = variable_user)
caja1.grid(row=1,column=2)
variable_pass = StringVar()
caja2 = Entry(ventana,textvariable = variable_pass, show='*')
caja2.grid(row=2,column=2)


ventana.mainloop()
