class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        self._precio = nuevo_precio

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id] = producto
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        productos_encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if productos_encontrados:
            for p in productos_encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("No hay productos en el inventario.")


def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un número entero.")


def obtener_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un número válido.")


def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto por ID")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("0. Salir")

        eleccion = input("Elige una opción: ")

        if eleccion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = obtener_entero("Cantidad del producto: ")
            precio = obtener_flotante("Precio del producto: ")
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif eleccion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif eleccion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Nuevo precio (deja en blanco para no cambiar): ")
            nueva_cantidad = int(cantidad) if cantidad else None
            nuevo_precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif eleccion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif eleccion == '5':
            inventario.mostrar_productos()

        elif eleccion == '0':
            print("Saliendo del sistema de gestión de inventarios.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
