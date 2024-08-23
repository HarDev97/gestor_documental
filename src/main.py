import tkinter as tk
from PIL import Image, ImageTk
from config import APP_TITLE, LOGO_PATH


def main():
    # Creando raíz
    root = tk.Tk()  # Crea ingterfaz
    root.title(APP_TITLE)

    # Cargando la imagen con PIL
    icon_path = LOGO_PATH
    img = Image.open(icon_path)
    icon = ImageTk.PhotoImage(img)
    root.iconphoto(False, icon)

    # Definiendo si es resizable
    root.resizable(0, 0)

    # Creando frame
    frame = tk.Frame(root)
    frame.pack()
    # Configurando frame
    frame.config(width=500, height=500, background="dark blue")

    root.mainloop()


if __name__ == "__main__":
    main()
