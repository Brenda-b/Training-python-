import sqlite3
conexion= sqlite3.connect("basededatos.db")
cursor= conexion.cursor()
cursor.execute ("CREATE TABLE productos (Id INTERGER, NombreDeProducto TEXT, Precio INTERGER) ")
conexion.commit()
conexion.close()