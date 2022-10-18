import sqlite3

miConexion=sqlite3.connect("Primera base")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

# variosproductos=[
#     ('CAMISETA', 20, 'DEPORTES'),
#     ('JARRON', 32, 'DEPORTES'),
#     ('CARRO', 15, 'JUGUETE')
# ]
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosproductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

productos=miCursor.fetchall()
for producto in productos:
    print(producto)

miConexion.commit()


miConexion.close()