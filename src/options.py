import tkinter as tk
from tkinter import filedialog as fd
from .menu import *
from .practica_singleton import *
from commons.helper import *

class Options:

    def open_file(self, mn):
        root = tk.Tk()
        root.withdraw()
        file = fd.askopenfilename(title='Open files', filetypes=[('text files', '*.txt *.lfp')])
        
        if file != "":
            PracticaSingleton().file = file
            print("Archivo cargado exitosamente\n")

        else:
            print("No se ha seleccionado ningun archivo\n")
        mn.create_menu()

    def searches(self):
        lista = PracticaSingleton().file
        x = open(lista, 'r')
        data = Helper().get_file_readed(x)

        result = ""
        for key, value in data.items():
            if value["BUSCAR"] is not False:
                result += key + ": " + value["DATA"] + " BUSQUEDA POSICIONES = "
                result += self.search_data_list(value["DATA"], value["BUSCAR"])
        return result

    def search_data_list(self, data, search):
        result = ""
        data_list = data.split(",")
        for searching in search.split(","):
            for i in range(len(data_list)):
                if searching == data_list[i]:
                    result += str(i + 1) + ","

        if result == "":
            result = "NO ENCONTRADO\n"
        else:
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
                data_list = value["DATA"].split(",")
                result += self.bubble_sort(data_list)
        return result

    def bubble_sort(self, data_list):
        result = ""
        for i in range(len(data_list)):
            for j in range(len(data_list) - 1):
                if int(data_list[j]) > int(data_list[j + 1]):
                    data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]

        for x in data_list:
            result += x + ","
        result = result[:-1]
        result += "\n"
                
        return result

    def deploy_all(self):
        lista = PracticaSingleton().file
        x = open(lista, 'r')
        data = Helper().get_file_readed(x)

        result = ""
        for key, value in data.items():
            if value["BUSCAR"] is not False:
                result += key + ": " + value["DATA"] + " BUSQUEDA POSICIONES = "
                result += self.search_data_list(value["DATA"], value["BUSCAR"])
            if value["ORDENAR"] is not False:
                result += key + " ORDENADOS = "
                data_list = value["DATA"].split(",")
                result += self.bubble_sort(data_list)
        return result

    def deploy_to_html(self):
        data = self.deploy_all()
        generated = Helper().generate_html(data)
        return generated
