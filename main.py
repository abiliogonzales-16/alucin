from sqlite3 import *


baseDeDatos = connect("ALUCIN.db")
cr = baseDeDatos.cursor()


cr.execute('''
CREATE TABLE IF NOT EXISTS palabras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palabra TEXT NOT NULL,
    descripcion TEXT NOT NULL)''')

baseDeDatos.commit()

def agregar(palabra, descripcion):
    cr.execute("INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)", (palabra, descripcion))
    baseDeDatos.commit()
    print(f" Palabra '{palabra}' agregada con éxito.")

print("Introduce palabras y sus descripciones")
while True:
    palabra = input("Palabra: ")
    if palabra.lower() == "salir":
        break
    descripcion = input("Descripción: ")
    agregar(palabra, descripcion)



baseDeDatos.close()
