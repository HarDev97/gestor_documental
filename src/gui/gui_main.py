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
        self.button_new = tk.Button(self, text="Guardar", command=self.save)
        self.button_new.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#dad5d6",
            bg="#158645",
            cursor="hand2",
            activebackground="#35bd6f",
        )
        self.button_new.grid(row=4, column=0, padx=10, pady=10)

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
