from PIL import Image, ImageTk
from gui.gui_main import Frame, navbar

import tkinter as tk
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
    # root.resizable(0, 0)
    # Invocando menu
    navbar(root)

    # Creando frame
    app = Frame(root=root)
    app.mainloop()


if __name__ == "__main__":
    main()
