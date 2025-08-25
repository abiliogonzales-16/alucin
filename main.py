from sqlite3 import *
from customtkinter import *

baseDeDatos = connect("ALUCIN.db")
cr = baseDeDatos.cursor()


cr.execute('''
CREATE TABLE IF NOT EXISTS palabras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palabra TEXT NOT NULL,
    descripcion TEXT NOT NULL)''')

baseDeDatos.commit()
baseDeDatos.close()


set_appearance_mode("dark")
set_default_color_theme("dark-blue")


# se cre el incio de la app
app = CTk ()
app.title("Ahogado")

#pantalla inicial ========
ventana_inicial = CTkFrame(app)
ventana_inicial.pack()

titulo = CTkLabel(ventana_inicial, text="Bienvenido ", font=("Arial", 20))
titulo.pack(pady=30)

btn_jugar = CTkButton(ventana_inicial, text="Jugar", width=200, height=40)
btn_jugar.pack(pady=10)

btn_salir = CTkButton(ventana_inicial, text="Salir", width=200, height=40, command=app.quit)
btn_salir.pack(pady=10)

#fin de la pantalla inicial
#==========

#ventana del juego inial =======
pantalla_juego = CTkFrame(app)

# Acciones
#
acciones = CTkFrame(pantalla_juego)
acciones.pack(pady=10, padx=10)

btn_salir = CTkButton(pantalla_juego, text="Salir", width=200, height=40, command=app.quit)
btn_salir.pack(pady=10)


CTkLabel(acciones, text="Acciones", font=("Arial", 16)).pack(anchor="w", padx=10)
CTkButton(acciones, text="Nueva palabra").pack(side="left", padx=5)
CTkButton(acciones, text="Agregar palabra").pack(side="left", padx=5)
CTkButton(acciones, text="Eliminar palabra").pack(side="left", padx=5)


#=============
#Información
info = CTkFrame(pantalla_juego)
info.pack(pady=10, fill="x", padx=10)

CTkLabel(info, text="Información", font=("Arial", 16)).pack(anchor="w", padx=10)
CTkLabel(info, text="Descripción: ...").pack(anchor="w", padx=10)
CTkLabel(info, text="Longitud: ...").pack(anchor="w", padx=10)
CTkLabel(info, text="Intentos restantes: ...").pack(anchor="w", padx=10)
#fin =========



# Jugar
jugar = CTkFrame(pantalla_juego)
jugar.pack(pady=10, fill="x", padx=10)

CTkLabel(jugar, text="Jugar", font=("Arial", 16)).pack(anchor="w", padx=10)
CTkEntry(jugar, width=200).pack(side="left", padx=10)
CTkButton(jugar, text="Comprobar").pack(side="left", padx=10)


# ========================
# Función para cambiar de pantalla
# ========================
#esto esta busado en GPT

def mostrar_juego():
    ventana_inicial.pack_forget()
    pantalla_juego.pack()

btn_jugar.configure(command=mostrar_juego)


app.mainloop()
