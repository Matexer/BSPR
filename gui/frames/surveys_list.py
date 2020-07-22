import tkinter as tk
import tkinter.ttk as ttk
from gui.elements import *
from .fuels_list import FuelsListFrame


class SurveysListFrame(FuelsListFrame):
    def __init__(self, top):
        ActionFrame.__init__(self, top)

        options_container = tk.Frame(self)
        self.cboxs, self.buttons = self.create_options(options_container)
        list_container = tk.Frame(self)
        tree = self.create_list(list_container)

        self.buttons[0].configure(command=lambda: top.change_frame(3))

        options_container.pack(side="top", fill="x", pady=5)
        list_container.pack(side="top", fill="both", expand=1)

        top.update()
        tree_width = top.winfo_width()
        tree.set_columns(("test 1 dddddddddddddddddddddkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkm", "test 2", "test 3"))
        tree.set_columns_width(tree_width, (0.6, 0.2, 0.2))

    def create_options(self, top):
        cbox_container = tk.Frame(top)
        cboxs = self.create_cboxs(cbox_container)
        buttons_container = tk.Frame(top)
        buttons = self.create_btns(buttons_container)
        cbox_container.pack(side="left")
        buttons_container.pack(side="right")
        return cboxs, buttons

    @staticmethod
    def create_cboxs(top):
        fuel_label = tk.Label(top)
        fuel_label.configure(text="Paliwo")
        fuel_cbox = ttk.Combobox(top)
        type_label = tk.Label(top)
        type_label.configure(text="Rodzaj pomiaru")
        type_cbox = ttk.Combobox(top)

        fuel_label.pack(side="left")
        fuel_cbox.pack(side="left")
        type_label.pack(side="left")
        type_cbox.pack(side="left")
        return fuel_cbox, type_cbox
