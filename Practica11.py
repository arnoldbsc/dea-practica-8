# Fetchone

import sqlite3


conn = sqlite3.connect('test.db')
print("Opened database successfully")
cur = conn.cursor()


cur.execute("SELECT * FROM MASCOTA;")
one_result = cur.fetchone()
print(one_result)
print("Consulta realizada satisfactoriamente");conn.close()

# Fetchmany

import sqlite3


conn = sqlite3.connect('test.db')
print("Opened database successfully")
cur = conn.cursor()


cur.execute("SELECT * FROM mascota;")
three_results = cur.fetchmany(3)
print(three_results)
print("Consulta realizada satisfactoriamente");conn.close()

# Fetchall

import sqlite3


conn = sqlite3.connect('test.db')
print("Opened database successfully")
cur = conn.cursor()


cur.execute("SELECT * FROM mascota;")
all_results = cur.fetchall()
print(all_results)
print("Consulta realizada satisfactoriamente")
conn.close()

# Unir tablas

import sqlite3


conn = sqlite3.connect('test.db')
print("Opened database successfully")
cur = conn.cursor()




conn.execute('''CREATE TABLE FAMILIA_MASCOTA
        (ID_FAMILIA INT PRIMARY     KEY     NOT NULL,
        NOMBRE_FAMILIA              TEXT    NOT NULL,
        NUMERO_MIEMBROS             INT     NOT NULL,
        MASCOTA_ID                  INT     NOT NULL,
        FOREIGN KEY (MASCOTA_ID)
            REFERENCES MASCOTA (ID) );''')
print("Table created successfully")


conn.execute("INSERT INTO FAMILIA_MASCOTA (ID_FAMILIA,NOMBRE_FAMILIA,NUMERO_MIEMBROS,MASCOTA_ID) \
      VALUES (102, 'LITTLE', 4, 2 )")
conn.execute("INSERT INTO FAMILIA_MASCOTA (ID_FAMILIA,NOMBRE_FAMILIA,NUMERO_MIEMBROS,MASCOTA_ID) \
      VALUES (103, 'CONOR', 4, 3 )")
conn.execute("INSERT INTO FAMILIA_MASCOTA (ID_FAMILIA,NOMBRE_FAMILIA,NUMERO_MIEMBROS,MASCOTA_ID) \
      VALUES (104, 'SMITH', 4, 4 )")
print("DATES REGISTER successfully")

# Uso de JOINS

import sqlite3


conn = sqlite3.connect('test.db')
print("Opened database successfully")
cur = conn.cursor()




cur.execute("" "SELECT nombre_masc, nombre_due, nombre_familia FROM mascota INNER JOIN familia_mascota ON familia_mascota.mascota_id  = mascota.id;" "")
result = cur.fetchall()
for row in result:
    print(row)
print("Consulta realizada satisfactoriamente")
conn.close()
