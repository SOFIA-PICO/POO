import tkinter as tk
from tkinter import ttk, messagebox


class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Tareas")
        self.master.geometry("420x380")
        self.master.configure(bg="#f0f0f0")

        self.task_data = []

        self.setup_ui()

    def setup_ui(self):
        # Etiqueta principal
        title = tk.Label(self.master, text="Mis Tareas", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        title.pack(pady=10)

        # Entrada de texto
        self.task_input = tk.Entry(self.master, width=40)
        self.task_input.pack(pady=5)
        self.task_input.bind("<Return>", self.handle_add_task)

        # Botón para añadir
        btn_add = tk.Button(self.master, text="Agregar", width=20, command=self.handle_add_task)
        btn_add.pack(pady=5)

        # Lista de tareas (Treeview con checkbox simulado)
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)
        self.tree = ttk.Treeview(self.master, columns=("Estado",), show="headings")
        self.tree.heading("Estado", text="Tarea")
        self.tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Botones de acción
        btn_frame = tk.Frame(self.master, bg="#f0f0f0")
        btn_frame.pack(pady=5)

        btn_done = tk.Button(btn_frame, text="Marcar como Hecha", width=18, command=self.handle_mark_done)
        btn_done.grid(row=0, column=0, padx=5)

        btn_remove = tk.Button(btn_frame, text="Eliminar Seleccionada", width=18, command=self.handle_remove)
        btn_remove.grid(row=0, column=1, padx=5)

        self.tree.bind("<Double-1>", self.handle_mark_done)

    def handle_add_task(self, event=None):
        tarea = self.task_input.get().strip()
        if tarea:
            self.task_data.append({"contenido": tarea, "hecha": False})
            self.refresh_tree()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Debes escribir una tarea primero.")

    def handle_mark_done(self, event=None):
        selected = self.tree.selection()
        if selected:
            index = int(selected[0])
            self.task_data[index]["hecha"] = not self.task_data[index]["hecha"]
            self.refresh_tree()
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para cambiar su estado.")

    def handle_remove(self):
        selected = self.tree.selection()
        if selected:
            index = int(selected[0])
            del self.task_data[index]
            self.refresh_tree()
        else:
            messagebox.showinfo("Sin selección", "Debes elegir una tarea para eliminar.")

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for idx, task in enumerate(self.task_data):
            text = task["contenido"]
            if task["hecha"]:
                text = f"[Hecha] {text}"
            self.tree.insert("", "end", iid=idx, values=(text,))


# Ejecutar aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = TaskManager(ventana)
    ventana.mainloop()
