import sqlite3
import random

# Conexión a la base de datos
baseDeDatos = sqlite3.connect("ALUCIN.db")
cursor = baseDeDatos.cursor()

# Crear la tabla de palabras si no existe
def crear_tabla():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            descripcion TEXT NOT NULL
        )
    ''')
    baseDeDatos.commit()

# Función para agregar palabras a la base de datos
def agregar_palabra(palabra, descripcion):
    # Validar que no estén vacíos
    if not palabra.strip() or not descripcion.strip():
        print("No puedes agregar palabras o descripciones vacías.")
        return

    # Verificar si la palabra ya existe en la base de datos
    cursor.execute("SELECT * FROM palabras WHERE palabra = ?", (palabra,))
    if cursor.fetchone():
        print("Esa palabra ya está registrada en la base de datos.")
        return


    cursor.execute("INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)", (palabra, descripcion))
    baseDeDatos.commit()
    print(f"La palabra '{palabra}' ha sido agregada correctamente.")

# Función para obtener una palabra aleatoria
def obtener_palabra_aleatoria():
    cursor.execute("SELECT palabra, descripcion FROM palabras")
    todas_las_palabras = cursor.fetchall()
    if todas_las_palabras:
        return random.choice(todas_las_palabras)
    else:
        return None

# Función para eliminar palabras
def eliminar_palabra(palabra):
    cursor.execute("DELETE FROM palabras WHERE palabra = ?", (palabra,))
    baseDeDatos.commit()
    print(f"La palabra '{palabra}' ha sido eliminada de la base de datos.")

# Cerrar la conexión con la base de datos
def cerrar_bd():
    baseDeDatos.close()

# Función principal
if __name__ == "__main__":
    crear_tabla()
    print("Bienvenido a la base de datos de ALUCION")
    while True:
        print("escribe (salir) para finalir el programa")
        palabra = input("¿Qué palabra deseas agregar?  ")
        if palabra.lower() == "salir":
            break
        descripcion = input("Escribe una descripción para la palabra: ")
        agregar_palabra(palabra, descripcion)
    cerrar_bd()
