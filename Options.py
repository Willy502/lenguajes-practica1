import tkinter as tk
from tkinter import filedialog as fd

class Options:

    def open_file(self):
        name = fd.askopenfilename()
        print(name)