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
                data_options = {}
                list_name = line.split("=")[0]
                to_trim_list = line.split("=")[1]
                
                if "ORDENAR" in to_trim_list:
                    data_options["ORDENAR"] = True

                    if "BUSCAR" not in to_trim_list:
                        data_options["BUSCAR"] = False
                        data_options["data"] = to_trim_list.split("ORDENAR")[0].strip()

                    else:
                        data_lists = to_trim_list.split("ORDENAR")
                        if "BUSCAR" not in data_lists[0]:
                            data_list = data_lists[0].strip()
                            data_options["BUSCAR"] = data_lists[1].split("BUSCAR")[1].strip()
                        else:
                            data_list = data_lists[0].split("BUSCAR")[0].strip()
                            data_options["BUSCAR"] = data_lists[0].split("BUSCAR")[1].strip()
                        data_options["data"] = data_list
                    
                    if data_options["BUSCAR"] != False:
                        if data_options["BUSCAR"][len(data_options["BUSCAR"]) - 1] == ",":
                            data_options["BUSCAR"] = data_options["BUSCAR"][:-1]
                    lists[list_name] = data_options
                    
                else:
                    data_options["ORDENAR"] = False
                    data_options["BUSCAR"] = False
                    if "BUSCAR" in to_trim_list:
                        data_list = to_trim_list.split("BUSCAR")[0].strip()
                        data_options["data"] = data_list
                        data_options["BUSCAR"] = to_trim_list.split("BUSCAR")[1].strip()

                    if data_options["BUSCAR"] != False:
                        if data_options["BUSCAR"][len(data_options["BUSCAR"]) - 1] == ",":
                            data_options["BUSCAR"] = data_options["BUSCAR"][:-1]
                    lists[list_name] = data_options
                    
            print(lists)
            print("Archivo cargado exitosamente\n")
            mn.create_menu()

        else:
            print("No se ha seleccionado ningun archivo\n")
            mn.create_menu()
