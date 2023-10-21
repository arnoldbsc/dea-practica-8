# Insertar

import sqlite3


conn = sqlite3.connect('test.db')
print ("Opened database successfully")


conn.execute("INSERT INTO MASCOTA (ID,NOMBRE_MASC,EDAD_MASC,NOMBRE_DUE,SALARIO_DUE) \
      VALUES (1, 'BUGGY', 12, 'HAROLD', 20000.00 )")
conn.execute("INSERT INTO MASCOTA (ID,NOMBRE_MASC,EDAD_MASC,NOMBRE_DUE,SALARIO_DUE) \
      VALUES (2, 'FAN', 14, 'RODRIGO', 15000.00 )")
conn.execute("INSERT INTO MASCOTA (ID,NOMBRE_MASC,EDAD_MASC,NOMBRE_DUE,SALARIO_DUE) \
      VALUES (3, 'CHAN', 16, 'OSCAR', 20000.00 )")
conn.execute("INSERT INTO MASCOTA (ID,NOMBRE_MASC,EDAD_MASC,NOMBRE_DUE,SALARIO_DUE) \
      VALUES (4, 'SAN', 10, 'GONZALO ', 65000.00 )")
conn.commit()
print ("Records created successfully")
conn.close()

# Seleccionar

import sqlite3


conn = sqlite3.connect('test.db')
print ("Opened database successfully")


cursor = conn.execute("SELECT id, nombre_masc, edad_masc, nombre_due from MASCOTA")
for row in cursor:
   print ("ID = ", row[0])
   print ("NOMBRE DE MASC = ", row[1])
   print ("EDAD DE MASCOTA = ", row[2])
   print ("DUEÑO = ", row[3], "\n")
   
print ("Operation done successfully")
conn.close()

# Actualizar

import sqlite3


conn = sqlite3.connect('test.db')
print("Opened database successfully")




conn.execute("UPDATE mascota set edad_masc = 30 where ID = 1")
conn.commit()
print("Total number of rows updated :"), conn.total_changes


cursor = conn.execute(
    "SELECT id, nombre_masc, edad_masc, nombre_due from MASCOTA")
for row in cursor:
   print("ID = ", row[0])
   print("NOMBRE DE MASC = ", row[1])
   print("EDAD DE MASCOTA = ", row[2])
   print("DUEÑO = ", row[3], "\n")


print("Operation done successfully")
conn.close()

# Eliminar

import sqlite3


conn = sqlite3.connect('test.db')
print("Opened database successfully")




conn.execute("DELETE from MASCOTA where ID = 2;")
conn.commit()
print("Total number of rows deleted :"), conn.total_changes


cursor = conn.execute(
    "SELECT id, nombre_masc, edad_masc, nombre_due from MASCOTA")
for row in cursor:
   print("ID = ", row[0])
   print("NOMBRE DE MASC = ", row[1])
   print("EDAD DE MASCOTA = ", row[2])
   print("DUEÑO = ", row[3], "\n")


print("Operation done successfully")
conn.close()
