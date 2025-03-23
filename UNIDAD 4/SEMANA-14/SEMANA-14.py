import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class GestorAgenda:
    def __init__(self, raiz):
        raiz.title("Gestor de Agenda")
        raiz.geometry("640x430")
        raiz.resizable(False, False)

        # Título
        self.titulo = tk.Label(raiz, text="Agenda Personal", font=("Arial", 16, "bold"))
        self.titulo.place(x=230, y=10)

        # Tabla de eventos
        self.tabla = ttk.Treeview(raiz, columns=("Fecha", "Hora", "Tarea"), show="headings")
        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Hora", text="Hora")
        self.tabla.heading("Tarea", text="Descripción")
        self.tabla.place(x=30, y=50, width=580, height=150)

        # Campos de entrada
        tk.Label(raiz, text="Fecha:").place(x=40, y=220)
        self.fecha = DateEntry(raiz, width=15)
        self.fecha.place(x=100, y=220)

        tk.Label(raiz, text="Hora:").place(x=40, y=260)
        self.hora = tk.Entry(raiz, width=20)
        self.hora.place(x=100, y=260)

        tk.Label(raiz, text="Descripción:").place(x=40, y=300)
        self.tarea = tk.Entry(raiz, width=40)
        self.tarea.place(x=130, y=300)

        # Botones con diseño personalizado
        self.boton_guardar = tk.Button(raiz, text="Añadir", width=12, bg="#0066CC", fg="white", command=self.anadir)
        self.boton_guardar.place(x=450, y=220)

        self.boton_borrar = tk.Button(raiz, text="Quitar Selección", width=15, bg="#CC0000", fg="white", command=self.borrar_evento)
        self.boton_borrar.place(x=450, y=260)

        self.boton_salir = tk.Button(raiz, text="Cerrar", width=10, command=raiz.quit)
        self.boton_salir.place(x=470, y=310)

    # Función para añadir evento
    def anadir(self):
        f = self.fecha.get()
        h = self.hora.get().strip()
        t = self.tarea.get().strip()

        if not f or not h or not t:
            messagebox.showwarning("Campos incompletos", "Completa todos los campos.")
            return

        self.tabla.insert("", "end", values=(f, h, t))
        self.hora.delete(0, tk.END)
        self.tarea.delete(0, tk.END)

    # Función para eliminar evento seleccionado
    def borrar_evento(self):
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showinfo("Sin selección", "Primero selecciona un evento.")
            return

        confirmacion = messagebox.askyesno("¿Eliminar?", "¿Seguro que deseas eliminar este evento?")
        if confirmacion:
            self.tabla.delete(seleccionado)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = GestorAgenda(ventana)
    ventana.mainloop()
