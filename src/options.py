import tkinter as tk
from tkinter import filedialog as fd
from .menu import *

class Options:

    def open_file(self, mn):
        root = tk.Tk()
        root.withdraw()
        file = fd.askopenfile(title='Open files', filetypes=[('text files', '*.txt')])
        if file is not None:
            for line in file:
                print(line)
        else:
            print("No se ha seleccionado ningun archivo\n")
            menu = mn.create_menu()