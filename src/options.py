import tkinter as tk
from tkinter import filedialog as fd
from .menu import *
from .practica_singleton import *
from commons.helper import *

class Options:

    def open_file(self, mn):
        root = tk.Tk()
        root.withdraw()
        file = fd.askopenfile(title='Open files', filetypes=[('text files', '*.txt')])

        if file is not None:
            PracticaSingleton.get_instance().file = file
            print("Archivo cargado exitosamente\n")

        else:
            print("No se ha seleccionado ningun archivo\n")
        mn.create_menu()
