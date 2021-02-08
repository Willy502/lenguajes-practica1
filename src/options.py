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

    def searchs(self):
        lista = PracticaSingleton.get_instance().file
        data = Helper().get_file_readed(lista)

        result = ""
        for key, value in data.items():
            if value["BUSCAR"] is not False:
                result += key + ": " + value["data"] + " BUSQUEDA POSICIONES="
                if value["BUSCAR"] in value["data"]:
                    data_list = value["data"].split(",")
                    for i in range(0, len(data_list)):
                        if value["BUSCAR"] == data_list[i]:
                            result += str(i + 1) + ","
                    result = result[:-1]
                    result += "\n"
                else:
                    result += "NO ENCONTRADO\n"
        return result
