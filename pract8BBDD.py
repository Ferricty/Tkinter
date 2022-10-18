import sqlite3

miConexion=sqlite3.connect("Gestion Productos")

miCursor=miConexion.cursor()

# miCursor.execute('''
#                  CREATE TABLE PRODUCTOS (
#                  CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
#                  NOMBRE_ARTICULO VARCHAR(50),
#                  PRECIO INTEGER,
#                  SECCION VARCHAR(20))
#                  ''')

# productos=[
#     ("AR01","PELOTA",20,"JUGUETES"),
#     ("AR02","PANTALON",15,"MODA"),
#     ("AR03","DESTORNILLADOR",15,"MODA"),
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)",productos)


# Mejorando base de datos


# miCursor.execute('''
#                  CREATE TABLE PRODUCTOS (
#                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                  NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#                  PRECIO INTEGER,
#                  SECCION VARCHAR(20))
#                  ''')

# productos=[
#     ("PELOTA",20,"JUGUETES"),
#     ("PANTALON",15,"MODA"),
#     ("DESTORNILLADOR",15,"MODA"),
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)

# miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR05','tren',34,'JUGUETES')")


#           Realizando consulta en la base de datos

# miCursor.execute("SELECT * FROM PRODUCTOS  WHERE SECCION='JUGUETES'")
# productos=miCursor.fetchall()
# print(productos)

#           Realizando update
# miCursor.execute("UPDATE PRODUCTOS SET PRECIO=100 WHERE NOMBRE_ARTICULO='PELOTA'")

#           Realizando delete
miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO='PELOTA'")

miConexion.commit()


miConexion.close()