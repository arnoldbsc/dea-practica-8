import math

def practicaA():
    limit = 6
    numList = []
    maxNum = None
    minNum = None
    for i in range(limit):
        inNum = input('Ingrese el numero: ')
        inNum = int(inNum)
        if minNum is None or minNum > inNum:
            minNum = inNum
        if maxNum is None or maxNum < inNum:
            maxNum = inNum
        numList.append(inNum)
    print('El numero mas cercano al medio es: ', numList[int(limit/2)])
    print('El numero mayor es: ', maxNum)
    print('El numero menor es: ', minNum)

def practicaB ():
    limit = int(input('Ingrese la cantidad de veces a validar el primo: '))
    limit -= 1
    while(True):
        num = int(input('Ingrese el numero: '))
        result = 'Es primo'
        for i in range(2, num):
            if num % i == 0:
                result = 'No es primo'
                break
        print(result)
        if limit == 0:
            break
        limit -= 1

def suma_lista(lista):
    total = sum(lista)
    return total

def distancia_euclidiana(coordenada1, coordenada2):
    x1, y1 = coordenada1
    x2, y2 = coordenada2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def saludar(nombre, saludo="Hola"):
    mensaje = f"{saludo}, {nombre}!"
    return mensaje

def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

def practicaC ():
    mi_lista = [1, 2, 3, 4, 5]
    resultado = suma_lista(mi_lista)
    print("La suma de la lista es:", resultado)
    coord1 = (1, 2)
    coord2 = (4, 6)
    dist = distancia_euclidiana(coord1, coord2)
    print("La distancia euclidiana es:", dist)
    print(saludar("Juan"))
    print(saludar("Ana", "Buenos días"))
    resultado = operaciones(10, 5)
    print("Suma:", resultado[0])
    print("Resta:", resultado[1])
    print("Multiplicación:", resultado[2])
    print("División:", resultado[3])

practicaA()
practicaB()
practicaC()