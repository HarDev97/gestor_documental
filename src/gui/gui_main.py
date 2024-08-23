import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Creando interfaz
class Frame(tk.Frame):
    # Definiendo constructor
    def __init__(self, root=None):
        # Heredando
        super().__init__(root, width=800, height=800)
        self.root = root
        self.pack()
        # self.config(bg="gray")
        self.form()
        self.gridview()

    # Creando formulario
    def form(self):

        # Definiendo labels
        self.label_trd = tk.Label(self, text="TRD: ")
        self.label_trd.config(font=("Arial", "18", "bold"))
        self.label_trd.grid(row=0, column=0, padx=10, pady=10)

        self.label_serie = tk.Label(self, text="Serie: ")
        self.label_serie.config(font=("Arial", "18", "bold"))
        self.label_serie.grid(row=1, column=0, padx=10, pady=10)

        # Definiendo entries
        self.trd = tk.StringVar()
        self.entry_trd = ttk.Combobox(self, state="readonly")
        self.entry_trd["values"] = [1, 2, 3]
        self.entry_trd.config(width=50, font=("Arial", 12))
        self.entry_trd.grid(row=0, column=1, padx=10, pady=10)

        self.entry_serie = ttk.Combobox(self, state="readonly")
        self.entry_serie["values"] = [1, 2, 3]
        self.entry_serie.config(width=50, font=("Arial", 12))
        self.entry_serie.grid(row=1, column=1, padx=10, pady=10)

        # Definiendo botones
        self.button_new = tk.Button(self, text="Registrar", command=self.save)
        self.button_new.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#188251",
            cursor="hand2",
            activebackground="#35bd6f",
        )
        self.button_new.grid(row=2, column=0, padx=10, pady=10)

    # Guardar datos
    def save(self):
        # Obtener el valor seleccionado
        value_trd = self.entry_trd.get()
        value_serie = self.entry_serie.get()

        # Validando campos diligenciados
        if value_trd and value_serie:
            print(f"Valores guardados: TRD={value_trd}, Serie={value_serie}")
            self.clean_fields()
            confirm = messagebox.askquestion(
                "Confirmación", "¿Deseas guardar el registro?"
            )
            if confirm:
                messagebox.showinfo("Éxito", "El registro se guardó correctamente.")

        else:
            messagebox.showerror("Error", "Ambos campos deben tener un valor.")

    # Vista de datos
    def gridview(self):
        self.table = ttk.Treeview(self, columns=("TRD", "Serie"))
        self.table.grid(row=3, column=0, columnspan=2)

        # Definiendo encabezado
        self.table.heading("#0", text="#")
        self.table.heading("#1", text="TRD")
        self.table.heading("#2", text="Serie")

        # Agregando valores de muestra
        self.table.insert("", 0, text="1", values=("2015", "23"))

        # Agregando botones de editar y eliminar
        self.button_edit = tk.Button(self, text="Editar")
        self.button_edit.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#0d6efd",
            cursor="hand2",
            activebackground="#35bd6f",
        )
        self.button_edit.grid(row=5, column=0, padx=10, pady=10)

        # Agregando botones de editar y eliminar
        self.button_delete = tk.Button(self, text="Eliminar")
        self.button_delete.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#bb2d3b",
            cursor="hand2",
            activebackground="#35bd6f",
        )
        self.button_delete.grid(row=5, column=1, padx=10, pady=10)

    # Limpiando campos
    def clean_fields(self):
        self.entry_trd.set("")
        self.entry_serie.set("")


# Creando menu
def navbar(root):
    navbar = tk.Menu(root)
    root.config(menu=navbar, width=300, height=300)

    # Definiendo inicio
    home = tk.Menu(navbar, tearoff=0)
    navbar.add_cascade(label="Inicio", menu=home)
    # Definiendo opciones de inicio
    home.add_command(label="Crear registro")
    home.add_command(label="Eliminar registro")
    home.add_command(label="Salir", command=root.destroy)

    # Definiendo consultas
    navbar.add_cascade(label="Consultas")
