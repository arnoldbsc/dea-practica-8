# estudiante.py

class Estudiante:
    def __init__(self, nombre, apellido, edad, matricula, pension):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.matricula = matricula
        self.pension = pension

    def ingresarDatos(self, nombre, apellido, edad, matricula, pension):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.matricula = matricula
        self.pension = pension

    def imprimirDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Matrícula: {self.matricula}")
        print(f"Pensión: {self.pension}")

    def matricular(self):
        print(f"{self.nombre} {self.apellido} ha sido matriculado.")

    def pagarPension(self, cantidad):
        print(f"{self.nombre} {self.apellido} ha pagado {cantidad} de pensión.")

# menu.py
from estudiante import Estudiante

def main():
    estudiante1 = Estudiante("", "", 0, "", 0)  # Instanciar un objeto de la clase Estudiante

    while True:
        print("\nMenú:")
        print("1. Ingresar datos del estudiante")
        print("2. Imprimir datos del estudiante")
        print("3. Matricular al estudiante")
        print("4. Pagar pensión")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            matricula = input("Matrícula: ")
            pension = float(input("Pensión: "))
            estudiante1.ingresarDatos(nombre, apellido, edad, matricula, pension)
        elif opcion == 2:
            estudiante1.imprimirDatos()
        elif opcion == 3:
            estudiante1.matricular()
        elif opcion == 4:
            cantidad = float(input("Ingrese la cantidad a pagar: "))
            estudiante1.pagarPension(cantidad)
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()