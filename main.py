import sqlite3
import random

# Conectamos con la base de datos (se crea si no existe)
conexion = sqlite3.connect("ALUCIN.db")
cursor = conexion.cursor()

# Creamos la tabla donde se guardarán las palabras y sus pistas
def tabla():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            descripcion TEXT NOT NULL
        )
    ''')
    conexion.commit()

# Agregamos una nueva palabra con su pista
def agregar(palabra, descripcion):
    if palabra.strip() == "" or descripcion.strip() == "":
        print("No se puede guardar algo vacío. Escribe bien la palabra y la pista.")
        return

    # Revisamos si ya existe
    cursor.execute("SELECT * FROM palabras WHERE palabra = ?", (palabra,))
    if cursor.fetchone():
        print("Esa palabra ya está guardada.")
        return

    # Si no existe, la guardamos
    cursor.execute("INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)", (palabra, descripcion))
    conexion.commit()
    print(f" Guardado: '{palabra}' con su pista.")

# Elegimos una palabra al azar para jugar
def aleatoria():
    cursor.execute("SELECT palabra, descripcion FROM palabras")
    todas = cursor.fetchall()
    if todas:
        return random.choice(todas)
    else:
        return None

# Si queremos borrar una palabra
def eliminar(palabra):
    cursor.execute("DELETE FROM palabras WHERE palabra = ?", (palabra,))
    conexion.commit()
    print(f" Se eliminó la palabra '{palabra}'.")

# Cerramos la conexión con la base de datos
def cerrar_bd():
    conexion.close()

# Si ejecutamos este archivo directamente, nos deja agregar palabras
if __name__ == "__main__":
    tabla()
    print(" agregar palabra y describri palabra")
    print("opcion para salir es: salir")
    while True:
        palabra = input("Palabra: ")
        if palabra.lower() == "salir":
            break
        descripcion = input("Pista: ")
        agregar(palabra, descripcion)
    cerrar_bd()
