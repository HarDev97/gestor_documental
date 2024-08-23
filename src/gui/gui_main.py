import tkinter as tk


# Creando interfaz
class Frame(tk.Frame):
    # Definiendo constructor
    def __init__(self, root=None):
        # Heredando
        super().__init__(root, width=1700, height=980)
        self.root = root
        self.pack()
        self.config(bg="gray")
