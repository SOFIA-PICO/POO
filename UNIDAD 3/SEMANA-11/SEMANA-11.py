import json


class Producto:
    def __init__(self, identificador, nombre, stock, precio):
        self.identificador = identificador
        self.nombre = nombre
        self.stock = stock
        self.precio = precio

    def to_dict(self):
        return {"identificador": self.identificador, "nombre": self.nombre, "stock": self.stock, "precio": self.precio}

    def __repr__(self):
        return f"[{self.identificador}] {self.nombre} - Cantidad: {self.stock}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, identificador, nombre, stock, precio):
        if identificador in self.productos:
            print("Error: El producto ya existe en el inventario.")
        else:
            self.productos[identificador] = Producto(identificador, nombre, stock, precio)
            print("Producto agregado correctamente.")

    def quitar_producto(self, identificador):
        if identificador in self.productos:
            del self.productos[identificador]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def modificar_producto(self, identificador, stock=None, precio=None):
        if identificador in self.productos:
            if stock is not None:
                self.productos[identificador].stock = stock
            if precio is not None:
                self.productos[identificador].precio = precio
            print("Producto modificado exitosamente.")
        else:
            print("Error: No se encontró el producto.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No hay productos con ese nombre.")

    def listar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_datos(self, archivo="datos_inventario.json"):
        with open(archivo, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.productos.items()}, f)
        print("Datos guardados correctamente.")

    def cargar_datos(self, archivo="datos_inventario.json"):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                self.productos = {k: Producto(**v) for k, v in datos.items()}
            print("Datos cargados correctamente.")
        except FileNotFoundError:
            print("No hay datos previos, iniciando inventario vacío.")


def menu():
    sistema = Inventario()
    sistema.cargar_datos()

    while True:
        print("\n--- GESTIÓN DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Modificar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Guardar y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            identificador = input("ID del producto: ")
            nombre = input("Nombre: ")
            stock = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            sistema.agregar_producto(identificador, nombre, stock, precio)

        elif opcion == "2":
            identificador = input("ID del producto a eliminar: ")
            sistema.quitar_producto(identificador)

        elif opcion == "3":
            identificador = input("ID del producto a modificar: ")
            stock = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            stock = int(stock) if stock else None
            precio = float(precio) if precio else None
            sistema.modificar_producto(identificador, stock, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            sistema.buscar_producto(nombre)

        elif opcion == "5":
            sistema.listar_productos()

        elif opcion == "6":
            sistema.guardar_datos()
            print("Cerrando programa...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
