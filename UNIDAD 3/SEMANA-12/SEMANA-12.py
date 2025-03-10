class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.historial_prestamos = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.catalogo = {}  # Almacena los libros con ISBN como clave
        self.usuarios_registrados = {}  # Almacena usuarios con su ID como clave

    def añadir_libro(self, libro):
        if libro.isbn not in self.catalogo:
            self.catalogo[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("Este libro ya existe en el catálogo.")

    def eliminar_libro(self, isbn):
        if isbn in self.catalogo:
            del self.catalogo[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no está en el catálogo.")

    def inscribir_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("Este usuario ya está inscrito.")

    def remover_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            if usuario.historial_prestamos:
                print("No se puede eliminar, el usuario tiene libros prestados.")
            else:
                del self.usuarios_registrados[id_usuario]
                print(f"Usuario con ID {id_usuario} eliminado del sistema.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.catalogo:
            usuario = self.usuarios_registrados[id_usuario]
            libro = self.catalogo.pop(isbn)
            usuario.historial_prestamos.append(libro)
            print(f"Libro prestado a {usuario.nombre}: {libro}")
        else:
            print("No se puede prestar, libro o usuario no encontrado.")

    def recibir_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            for libro in usuario.historial_prestamos:
                if libro.isbn == isbn:
                    usuario.historial_prestamos.remove(libro)
                    self.catalogo[isbn] = libro
                    print(f"Libro devuelto: {libro}")
                    return
            print("El usuario no tenía este libro en préstamo.")
        else:
            print("Usuario no registrado.")

    def buscar_libro(self, texto):
        resultados = [libro for libro in self.catalogo.values() if
                      texto.lower() in libro.info[0].lower() or texto.lower() in libro.info[
                          1].lower() or texto.lower() in libro.categoria.lower()]

        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron coincidencias.")

    def mostrar_prestamos(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            if usuario.historial_prestamos:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.historial_prestamos:
                    print(libro)
            else:
                print("Este usuario no tiene libros en préstamo.")
        else:
            print("Usuario no registrado.")


# Pruebas del sistema
biblioteca = Biblioteca()
libro_a = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "1111111111")
libro_b = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "2222222222")
usuario_x = Usuario("Juan", "A001")

biblioteca.inscribir_usuario(usuario_x)
biblioteca.añadir_libro(libro_a)
biblioteca.añadir_libro(libro_b)
biblioteca.prestar_libro("A001", "1111111111")
biblioteca.mostrar_prestamos("A001")
biblioteca.recibir_libro("A001", "1111111111")
