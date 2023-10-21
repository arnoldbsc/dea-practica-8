# Abrir un archivo y leer su contenido
def file_read(fname):
    # Abrir el archivo especificado
    txt = open(fname)
    # Leer el contenido del archivo y mostrarlo en la consola
    print(txt.read())

# Llamar a la función con el archivo 'test.txt'
file_read('test.txt')

# Leer las primeras N líneas de un archivo
def file_read_from_head(fname, nlines):
    # Importar la función 'islice' desde el módulo 'itertools'
    from itertools import islice
    # Abrir el archivo especificado
    with open(fname) as f:
        # Usar 'islice' para leer las primeras N líneas y mostrarlas en la consola
        for line in islice(f, nlines):
            print(line)

# Llamar a la función con el archivo 'test.txt' y 2 líneas
file_read_from_head('test.txt', 2)

# Leer y mostrar todas las líneas de un archivo
def file_read(fname):
    # Abrir el archivo especificado en modo lectura
    with open(fname, "r") as myfile:
        # Leer todas las líneas y almacenarlas en una lista
        data = myfile.readlines()
        # Mostrar la lista de líneas en la consola
        print(data)

# Llamar a la función con el archivo 'test.txt'
file_read('test.txt')

# Importar la biblioteca 'glob' para trabajar con nombres de archivo
import glob

# Crear una lista para almacenar el contenido de varios archivos
char_list = []

# Obtener una lista de archivos con extensión '.txt' en el directorio actual
files_list = glob.glob("*.txt")

# Recorrer la lista de archivos
for file_elem in files_list:
    # Abrir cada archivo en modo lectura
    with open(file_elem, "r") as f:
        # Leer el contenido de cada archivo y agregarlo a la lista
        char_list.append(f.read())

# Mostrar la lista que contiene el contenido de los archivos
print(char_list)
