import tkinter as tk
from tkinter import filedialog as fd
from .menu import *
from .practica_singleton import *
from commons.helper import *

class Options:

    def open_file(self, mn):
        root = tk.Tk()
        root.withdraw()
        file = fd.askopenfilename(title='Open files', filetypes=[('text files', '*.txt')])

        if file is not None:
            PracticaSingleton().file = file
            print("Archivo cargado exitosamente\n")

        else:
            print("No se ha seleccionado ningun archivo\n")
        mn.create_menu()

    def searchs(self):
        lista = PracticaSingleton().file
        x = open(lista, 'r')
        data = Helper().get_file_readed(x)

        result = ""
        for key, value in data.items():
            if value["BUSCAR"] is not False:
                result += key + ": " + value["data"] + " BUSQUEDA POSICIONES = "
                if value["BUSCAR"] in value["data"]:
                    data_list = value["data"].split(",")
                    for i in range(len(data_list)):
                        if value["BUSCAR"] == data_list[i]:
                            result += str(i + 1) + ","
                    result = result[:-1]
                    result += "\n"
                else:
                    result += "NO ENCONTRADO\n"
        return result

    def bubble_sort(self, data_list):
        result = ""
        for i in range(len(data_list)):
            for j in range(len(data_list) - 1):
                if data_list[j] > data_list[j + 1]:
                    data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]

        for x in data_list:
            result += x + ","
        result = result[:-1]
        result += "\n"
                
        return result

    def order(self):
        lista = PracticaSingleton().file
        x = open(lista, 'r')
        data = Helper().get_file_readed(x)

        result = ""
        for key, value in data.items():
            if value["ORDENAR"] is not False:
                result += key + " ORDENADOS = "
                data_list = value["data"].split(",")
                result += self.bubble_sort(data_list)
        return result
