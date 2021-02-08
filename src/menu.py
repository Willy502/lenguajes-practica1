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
        print("3. Desplegar búsquedas")
        print("4. Desplegar todas")
        print("5. Desplegar todas a archivo")
        print("6. Salir")
        print("> ", end='')
        answer = input()
        print("------------------------------------\n")
        self.select_menu_option(answer)

    def select_menu_option(self, option):
        if option in ["2", "3", "4", "5"]:
            if PracticaSingleton().file is None:
                print("Para acceder a estas opciones primero debes cargar un archivo\n")
                self.create_menu()

        if option == "1":
            open_file = Options().open_file(self)
        elif option == "2":
            order = Options().order()
            print(order)
        elif option == "3":
            search = Options().searchs()
            print(search)
        elif option == "4":
            d_all = Options().deploy_all()
            print(d_all)
        elif option == "5":
            print(option)
        elif option == "6":
            quit()
        else:
            print("Selecciona una opción válida\n")
        self.create_menu()
