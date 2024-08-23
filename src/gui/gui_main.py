import tkinter as tk


# Creando interfaz
class Frame(tk.Frame):
    # Definiendo constructor
    def __init__(self, root=None):
        # Heredando
        super().__init__(root, width=800, height=800)
        self.root = root
        self.pack()
        self.config(bg="gray")


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
