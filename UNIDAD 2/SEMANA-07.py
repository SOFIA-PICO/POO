# Clase que representa un archivo que puede ser leído o escrito
class Archivo:
    # Constructor (__init__)
    def __init__(self, nombre, modo):
        """
        Constructor de la clase Archivo.
        Inicializa el nombre del archivo y el modo de apertura.
        También abre el archivo.
        """
        self.nombre = nombre
        self.modo = modo
        self.archivo = None
        try:
            self.archivo = open(nombre, modo)
            print(f"Archivo '{nombre}' abierto en modo '{modo}'.")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")

    # Método para escribir en el archivo
    def escribir(self, texto):
        """
        Escribe el texto dado en el archivo si está en modo escritura.
        """
        if self.archivo and 'w' in self.modo:
            self.archivo.write(texto)
            print(f"Texto escrito en el archivo '{self.nombre}'.")
        else:
            print("El archivo no está en modo escritura.")

    # Método para leer el archivo
    def leer(self):
        """
        Lee el contenido del archivo si está en modo lectura.
        """
        if self.archivo and 'r' in self.modo:
            contenido = self.archivo.read()
            print(f"Contenido del archivo '{self.nombre}':")
            print(contenido)
            return contenido
        else:
            print("El archivo no está en modo lectura.")

    # Destructor (__del__)
    def __del__(self):
        """
        Destructor de la clase Archivo.
        Se asegura de cerrar el archivo si está abierto.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre}' cerrado correctamente.")

# Programa principal para demostrar el uso de la clase
if __name__ == "__main__":
    # Crear un archivo y escribir en él
    archivo_escritura = Archivo("ejemplo.txt", "w")
    archivo_escritura.escribir("Este es un ejemplo de uso de constructores y destructores en Python.\n")
    del archivo_escritura  # Forzar la destrucción del objeto para cerrar el archivo

    # Leer el contenido del archivo
    archivo_lectura = Archivo("ejemplo.txt", "r")
    archivo_lectura.leer()
    del archivo_lectura  # Forzar la destrucción del objeto para cerrar el archivo
