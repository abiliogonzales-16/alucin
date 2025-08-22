from tkinter import  *

def juggar():
    ventana = Toplevel(app)
    etiqueta = Label(ventana,text="kfjhskfjh")
    ventana.title("ventana emergente")
    etiqueta.pack()


# no esta en uso

def salir ():
    sali = ventana.destroy



'''
def calculate():
    resul = eval(caja1.get())
    caja1.delete(0, END)
    caja1.insert(END, str(resul))

otro.pop(actual)
            cuaderno.forget(actual)
'''


app = Tk ()

app.title("Ahogado")

ventana = Tk

btn = Button(app,text="jugar ",command=juggar)
btn1 = Button(app,text="salir ", command=salir )

btn1.pack()
btn.pack()
app.mainloop()