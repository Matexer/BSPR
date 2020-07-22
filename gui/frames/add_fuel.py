import tkinter as tk
from gui.elements import InputTable


class AddFuelFrame(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)
        variables = (("atttttttttttt", "b", "c"),
                     ("e", "f", "h"))
        properties = {"ipadx": 0,
                      "ipady": 0,
                      "padx": 5,
                      "pady": 5,
                      "sticky": "W"}
        table = InputTable(self, variables)
