import tkinter as tk
from tkinter import filedialog as fd

class Options:

    def open_file(self):
        file = fd.askopenfile(title='Open files', filetypes=[('text files', '*.txt')])
        for line in file:
            print(line)