import sqlite3
import random

# Conexión a la base de datos
baseDeDatos = sqlite3.connect("ALUCIN.db")
cursor = baseDeDatos.cursor()

# Crear tabla si no existe
def crear_tabla():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            descripcion TEXT NOT NULL
        )
    ''')
    baseDeDatos.commit()

# Agregar palabra
def agregar_palabra(palabra, descripcion):
    if not palabra.strip() or not descripcion.strip():
        return "Campos vacíos"
    cursor.execute("SELECT * FROM palabras WHERE palabra = ?", (palabra,))
    if cursor.fetchone():
        return "Duplicado"
    cursor.execute("INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)", (palabra, descripcion))
    baseDeDatos.commit()
    return "Agregado"

# Eliminar palabra
def eliminar_palabra(palabra):
    cursor.execute("DELETE FROM palabras WHERE palabra = ?", (palabra,))
    baseDeDatos.commit()
    return "Eliminado"

# Obtener palabra aleatoria
def obtener_palabra_aleatoria():
    cursor.execute("SELECT palabra, descripcion FROM palabras")
    todas = cursor.fetchall()
    return random.choice(todas) if todas else None

# Cerrar conexión
def cerrar_bd():
    baseDeDatos.close()

# Inicializar tabla al importar
crear_tabla()
