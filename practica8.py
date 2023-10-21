# estudiante.py

class Estudiante:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, nombre, apellido, edad, matricula, pension):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._matricula = matricula
        self._pension = pension

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, nueva_matricula):
        self._matricula = nueva_matricula

    @property
    def pension(self):
        return self._pension

    @pension.setter
    def pension(self, nueva_pension):
        self._pension = nueva_pension

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

    @classmethod
    def metodoClase1(cls):
        print("Este es el primer método de clase.")

    @classmethod
    def metodoClase2(cls):
        print("Este es el segundo método de clase.")

    @staticmethod
    def metodoStatic1():
        print("Este es el primer método estático.")

    @staticmethod
    def metodoStatic2():
        print("Este es el segundo método estático.")

    def __del__(self):
        print(f"El estudiante {self.nombre} {self.apellido} ha sido eliminado.")


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
        print("5. Ejecutar método de clase 1")
        print("6. Ejecutar método de clase 2")
        print("7. Ejecutar método estático 1")
        print("8. Ejecutar método estático 2")
        print("9. Salir")

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
            Estudiante.metodoClase1()
        elif opcion == 6:
            Estudiante.metodoClase2()
        elif opcion == 7:
            Estudiante.metodoStatic1()
        elif opcion == 8:
            Estudiante.metodoStatic2()
        elif opcion == 9:
            del estudiante1  # Llamar al destructor para eliminar el objeto
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
