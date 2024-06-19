from tkinter import * 

def mensaje():
    label3 = Label(ventana,text="Clave invalida") 
    label3.grid(row=4,column=2) 

ventana = Tk()
ventana.title('Ejemplo')
ventana.geometry("500x300")
label1 = Label(ventana,text="User name") 
label1.grid(row=1,column=1) 
label2 = Label(ventana,text="Password") 
label2.grid(row=2,column=1) 
variable_user = StringVar()
caja1 = Entry(ventana,textvariable = variable_user)
caja1.grid(row=1,column=2)
variable_pass = StringVar()
caja2 = Entry(ventana,textvariable = variable_pass, show='*')
caja2.grid(row=2,column=2)

boton1 = Button(ventana,text="Enter", command=mensaje)
boton1.grid(row=3,column=3)

ventana.mainloop()
