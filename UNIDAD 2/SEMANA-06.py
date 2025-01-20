# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca  # Atributo privado para demostrar encapsulación
        self.modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        self.__marca = valor  # Aquí podrías añadir validación si es necesario

    def describir(self):
        return f"Este es un vehículo marca {self.marca} modelo {self.modelo}."

    def encender(self):
        return "El vehículo está encendiendo."

# Clase derivada Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_de_puertas):
        super().__init__(marca, modelo)  # Llama al constructor de la clase base
        self.numero_de_puertas = numero_de_puertas

    # Método sobrescrito para demostrar polimorfismo
    def encender(self):
        return "El coche está encendiendo con un sonido único."

# Creando instancias de las clases
mi_vehiculo = Vehiculo("Toyota", "Corolla")
mi_coche = Coche("Honda", "Civic", 4)

# Utilizando métodos de las instancias creadas para demostrar funcionalidad
print(mi_vehiculo.describir())
print(mi_vehiculo.encender())
print(mi_coche.describir())
print(mi_coche.encender())