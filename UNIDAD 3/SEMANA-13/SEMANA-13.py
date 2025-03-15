import tkinter as tk
from tkinter import messagebox, ttk

def agregar_dato():
    dato = entrada.get().strip()
    if dato:
        tabla.insert("", "end", values=(dato,))
        entrada.delete(0, tk.END)
        actualizar_contador()
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar un dato válido.")

def limpiar_datos():
    for item in tabla.get_children():
        tabla.delete(item)
    actualizar_contador()

def eliminar_seleccionado():
    seleccionado = tabla.selection()
    if seleccionado:
        for item in seleccionado:
            tabla.delete(item)
        actualizar_contador()
    else:
        messagebox.showwarning("Advertencia", "Seleccione un elemento para eliminar.")

def actualizar_contador():
    total = len(tabla.get_children())
    contador_label.config(text=f"Total de elementos: {total}")

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Datos")
ventana.geometry("420x350")

# Frame para entrada y botones
frame = tk.Frame(ventana)
frame.grid(row=0, column=0, padx=10, pady=10)

# Etiqueta y campo de texto
tk.Label(frame, text="Ingrese un dato:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
entrada = tk.Entry(frame, font=("Arial", 12))
entrada.grid(row=0, column=1, padx=5, pady=5)

# Botones
tk.Button(frame, text="Agregar", command=agregar_dato, font=("Arial", 12)).grid(row=1, column=0, pady=5)
tk.Button(frame, text="Eliminar", command=eliminar_seleccionado, font=("Arial", 12)).grid(row=1, column=1, pady=5)
tk.Button(frame, text="Limpiar Todo", command=limpiar_datos, font=("Arial", 12)).grid(row=1, column=2, pady=5)

# Tabla para mostrar datos
tabla = ttk.Treeview(ventana, columns=("Dato",), show="headings", height=8)
tabla.heading("Dato", text="Datos ingresados")
tabla.column("Dato", width=300)
tabla.grid(row=1, column=0, padx=10, pady=10)

# Contador de elementos
contador_label = tk.Label(ventana, text="Total de elementos: 0", font=("Arial", 12))
contador_label.grid(row=2, column=0, pady=5)

ventana.mainloop()
