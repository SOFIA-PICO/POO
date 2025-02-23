import os
import json


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w") as f:
                json.dump({}, f)
        try:
            with open(self.archivo, "r") as f:
                self.productos = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error: No se pudo cargar el inventario. Archivo corrupto o inexistente.")
            self.productos = {}
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo de inventario.")

    def guardar_en_archivo(self):
        """Guarda los productos en el archivo después de cada modificación."""
        try:
            with open(self.archivo, "w") as f:
                json.dump(self.productos, f, indent=4)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado al guardar el archivo: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        """Añade un producto al inventario."""
        if nombre in self.productos:
            print(f"El producto '{nombre}' ya existe. Usa actualizar_producto para modificarlo.")
            return
        self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
        self.guardar_en_archivo()
        print(f"Producto '{nombre}' añadido correctamente.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        """Actualiza la cantidad y/o el precio de un producto existente."""
        if nombre not in self.productos:
            print(f"El producto '{nombre}' no existe en el inventario.")
            return
        if cantidad is not None:
            self.productos[nombre]["cantidad"] = cantidad
        if precio is not None:
            self.productos[nombre]["precio"] = precio
        self.guardar_en_archivo()
        print(f"Producto '{nombre}' actualizado correctamente.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre not in self.productos:
            print(f"El producto '{nombre}' no existe en el inventario.")
            return
        del self.productos[nombre]
        self.guardar_en_archivo()
        print(f"Producto '{nombre}' eliminado correctamente.")

    def mostrar_inventario(self):
        """Muestra todos los productos del inventario."""
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("Inventario:")
        for nombre, datos in self.productos.items():
            print(f"{nombre}: Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")


# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
