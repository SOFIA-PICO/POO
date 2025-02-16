class Producto:
    """
    Representa un producto dentro del inventario.
    """
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad disponible del producto."""
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        """Modifica el precio del producto."""
        self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    """
    Gestiona el inventario de productos.
    """
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        """Añade un producto nuevo si su ID no está registrado."""
        if producto.id_producto in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario según su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Modifica la cantidad y/o precio de un producto."""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por coincidencia parcial en el nombre."""
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """Muestra todos los productos registrados."""
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")


def solicitar_entero(mensaje):
    """Solicita un número entero al usuario asegurando una entrada válida."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")


def solicitar_flotante(mensaje):
    """Solicita un número decimal al usuario asegurando una entrada válida."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingrese un número válido.")


def menu():
    """Interfaz interactiva para la gestión del inventario."""
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = solicitar_entero("Cantidad: ")
            precio = solicitar_flotante("Precio: ")
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")
            inventario.actualizar_producto(id_producto,
                                           int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '0':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Inténtelo nuevamente.")


if __name__ == "__main__":
    menu()
