from sqlite3 import *


baseDeDatos = connect("ALUCIN.db")
cr = baseDeDatos.cursor()


cr.execute('''
CREATE TABLE IF NOT EXISTS palabras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palabra TEXT NOT NULL,
    descripcion TEXT NOT NULL)''')

baseDeDatos.commit()
baseDeDatos.close()
