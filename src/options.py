import tkinter as tk
from tkinter import filedialog as fd
from .menu import *
from .practica_singleton import *

class Options:

    def open_file(self, mn):
        root = tk.Tk()
        root.withdraw()
        file = fd.askopenfile(title='Open files', filetypes=[('text files', '*.txt')])
        if file is not None:
            lists = {}
            for line in file:

                list_name = line.split("=")[0]
                to_trim_list = line.split("=")[1]
                
                if "ORDENAR" in to_trim_list:
                    if "BUSCAR" not in to_trim_list:
                        data_list = to_trim_list.split("ORDENAR")[0].strip()
                        lists[list_name] = data_list
                    else:
                        data_lists = to_trim_list.split("ORDENAR")
                        if "BUSCAR" not in data_lists[0]:
                            data_list = data_lists[0].strip()
                            lists[list_name] = data_list
                        else:
                            data_list = data_lists[0].split("BUSCAR")[0].strip()
                            lists[list_name] = data_list
                else:
                    if "BUSCAR" in to_trim_list:
                        data_list = to_trim_list.split("BUSCAR")[0].strip()
                        lists[list_name] = data_list
                    

            print(lists)

            print("Archivo cargado exitosamente\n")
            mn.create_menu()

        else:
            print("No se ha seleccionado ningun archivo\n")
            mn.create_menu()
