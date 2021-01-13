import sqlite3
conexion= sqlite3.connect("basededatos.db")
cursor=conexion.cursor()
lista_de_productos= [(1,'impresora',300),(2,'raton',20),(3,'ordenador',600)]
cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", lista_de_productos)
conexion.commit()
cursor.execute("SELECT*FROM PRODUCTOS")
productos=cursor.fetchall()
for PRODUCTOS in productos:
    print(PRODUCTOS)
conexion.close()