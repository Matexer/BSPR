import tkinter as tk
from gui.elements import InputTable


class AddFuelFrame(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)

        table = self.create_inputs_container()
        table.pack(side="top", anchor="w")

    def create_inputs_container(self):
        variables = (("Średnica zewnętrzna ładunku paliwa [mm]",
                      "Średnica wewnętrzna ładunku paliwa [mm]",
                      "Długość ładunku paliwa [mm]",
                      "Masa paliwa [g]"),
                     ("f", "h"))
        properties = {"ipadx": 0,
                      "ipady": 0,
                      "padx": 5,
                      "pady": 5,
                      "sticky": "W"}
        table = InputTable(self, variables)
        return table

