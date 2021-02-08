from .options import *
from .practica_singleton import *
from commons.helper import *

class Menu:

    def __init__(self):
        self.create_menu()

    def create_menu(self):
        print("Menu Principal")
        print("Selecciona una opción a continuación")
        print("1. Cargar archivo de entrada")
        print("2. Desplegar listas ordenadas")
        print("3. Despleagar búsquedas")
        print("4. Desplegar todas")
        print("5. Desplegar todas a archivo")
        print("6. Salir")
        print("> ", end='')
        answer = input()
        print("------------------------------------\n")
        self.select_menu_option(answer)

    def select_menu_option(self, option):
        if option == "1":
            open_file = Options().open_file(self)
        elif option == "2":
            lista = PracticaSingleton.get_instance().file
            print(Helper().get_file_readed(lista))
        elif option == "3":
            print(option)
        elif option == "4":
            print(option)
        elif option == "5":
            print(option)
        elif option == "6":
            quit()
        else:
            print("Selecciona una opción válida\n")
            self.create_menu()
