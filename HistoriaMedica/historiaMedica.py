import tkinter as tk
from paciente.gui import Frame


def main():  # funcion principal del programa (ventana principal)

    root = tk.Tk()  # ventana principal
    root.title("Historia Medica")
    root.resizable(0,0)

    app = Frame(root)
    app.pack()  # Asegura que el Frame se muestre
    root.mainloop()  # El bucle principal debe ser sobre root




if __name__ == "__main__":   # si el archivo se ejecuta directamente, se ejecuta la funcion main
    main()