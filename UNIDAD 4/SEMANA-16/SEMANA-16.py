import tkinter as tk
from tkinter import messagebox, font

# Lista de tareas
tareas = []

# Inicializar ventana
ventana = tk.Tk()
ventana.title("Tareas Diarias")
ventana.geometry("500x540")
ventana.config(bg="#ffffff")

# ---------- FUENTES Y ESTILOS ----------
fuente_tarea = font.Font(family="Helvetica", size=12)
fuente_tachada = font.Font(family="Helvetica", size=12, overstrike=1)

# ---------- WIDGETS ----------

# Campo para escribir nueva tarea
entrada_tarea = tk.Entry(ventana, width=40, font=fuente_tarea)
entrada_tarea.pack(pady=5)

# Campo para ingresar número de tarea (completar/eliminar)
entrada_numero = tk.Entry(ventana, width=10, font=fuente_tarea, justify="center")
entrada_numero.pack(pady=5)

# Zona para mostrar tareas
zona_tareas = tk.Text(ventana, width=55, height=20, font=fuente_tarea)
zona_tareas.pack(pady=10)
zona_tareas.config(state=tk.DISABLED)

# Estilos de texto en zona_tareas
zona_tareas.tag_configure("pendiente", foreground="black", font=fuente_tarea)
zona_tareas.tag_configure("completada", foreground="green", font=fuente_tachada)

# ---------- FUNCIONES ----------

def mostrar_tareas():
    zona_tareas.config(state=tk.NORMAL)
    zona_tareas.delete("1.0", tk.END)
    for i, t in enumerate(tareas):
        estado = "[✓]" if t["completada"] else "[ ]"
        linea = f"{i+1}. {estado} {t['texto']}\n"
        tag = "completada" if t["completada"] else "pendiente"
        zona_tareas.insert(tk.END, linea, tag)
    zona_tareas.config(state=tk.DISABLED)

def agregar(event=None):
    texto = entrada_tarea.get().strip()
    if texto:
        tareas.append({"texto": texto, "completada": False})
        entrada_tarea.delete(0, tk.END)
        mostrar_tareas()
    else:
        messagebox.showwarning("Campo vacío", "Por favor escribe una tarea.")

def completar(event=None):
    try:
        num = int(entrada_numero.get()) - 1
        if 0 <= num < len(tareas):
            tareas[num]["completada"] = not tareas[num]["completada"]
            mostrar_tareas()
            entrada_numero.delete(0, tk.END)
        else:
            messagebox.showerror("Número inválido", "No hay tarea con ese número.")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Debes ingresar un número.")

def eliminar(event=None):
    try:
        num = int(entrada_numero.get()) - 1
        if 0 <= num < len(tareas):
            tareas.pop(num)
            mostrar_tareas()
            entrada_numero.delete(0, tk.END)
        else:
            messagebox.showerror("Número inválido", "No hay tarea con ese número.")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Debes ingresar un número.")

def salir(event=None):
    ventana.quit()

# ---------- BOTONES ----------

frame_botones = tk.Frame(ventana, bg="#ffffff")
frame_botones.pack(pady=5)

tk.Button(frame_botones, text="Agregar", width=12, command=agregar, bg="#aeeaae").grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Completar", width=12, command=completar, bg="#add8e6").grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Eliminar", width=12, command=eliminar, bg="#f08080").grid(row=0, column=2, padx=5)

# ---------- ATAJOS DE TECLADO ----------
ventana.bind("<Return>", agregar)
ventana.bind("<c>", completar)
ventana.bind("<C>", completar)
ventana.bind("<d>", eliminar)
ventana.bind("<D>", eliminar)
ventana.bind("<Escape>", salir)

# ---------- INICIAR APP ----------
ventana.mainloop()
