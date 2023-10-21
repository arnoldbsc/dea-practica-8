#A

archivo_texto = open("mi_archivo.txt", "w")
archivo_binario = open("mi_archivo.bin", "wb")
def escribir_linea(archivo, linea):
    archivo.write(linea + "\n")
while True:
    texto = input("Escribe una línea (o escribe 'fin' para terminar): ")
    if texto.lower() == 'fin':
        break
    escribir_linea(archivo_texto, texto)
    escribir_linea(archivo_binario, bytes(texto, 'utf-8'))
archivo_texto.close()
archivo_binario.close()

#B

def file_read(fname):
    with open(fname, "w") as myfile:
        myfile.write("Ejercicios Python\n")
        myfile.write("Ejercicios Java")

file_read('abc.txt') 
with open('abc.txt') as txt:
    print(txt.read())