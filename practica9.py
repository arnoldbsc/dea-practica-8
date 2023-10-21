# A

import sqlite3

conn = sqlite3.connect('pedidos.db')

conn = sqlite3.connect(':memory:')

cur = conn.cursor()

cur.execute("CREATE TABLE pedidos (id INTEGER PRIMARY KEY, producto TEXT, cantidad INTEGER)")

conn.commit()
conn.close()

# B

#!/usr/bin/python
import sqlite3

conn = sqlite3.connect('ORDERS.db')
print("Base de datos abierta satisfactoriamente")

# C

import sqlite3

# Crear una conexión a la base de datos
conn = sqlite3.connect('ORDERS.db')
print("Base de datos abierta satisfactoriamente")

# Crear un objeto cursor
cur = conn.cursor()

# Crear la tabla 'users' si no existe
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        userid INT PRIMARY KEY,
        fname TEXT,
        lname TEXT,
        gender TEXT
    );
""")
conn.commit()

# Crear la tabla 'orders' si no existe
cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        orderid INT PRIMARY KEY,
        date TEXT,
        userid INT,
        total TEXT
    );
""")
conn.commit()

# Cerrar la conexión
conn.close()
