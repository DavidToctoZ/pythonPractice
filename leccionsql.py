import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad integer, email varchar(100))")

#cursor.execute("INSERT INTO usuarios VALUES ('Hector', 27, 'dt@g.com')")
cursor.execute("SELECT * FROM usuarios")
print(cursor)

usuario = cursor.fetchone()
print(usuario)
conexion.commit()
conexion.close()
