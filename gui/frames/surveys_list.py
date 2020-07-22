import tkinter as tk
import tkinter.ttk as ttk
from gui.elements import *
from .fuels_list import FuelsListFrame


class SurveysListFrame(ActionFrame):
    def __init__(self, top):
        ActionFrame.__init__(self, top)

        list_container, tree = self.create_list_container()

        self.buttons[0].configure(command=lambda: top.change_frame(3))

        btn_container.pack(side="top", anchor="e", pady=5)
        list_container.pack(side="top", fill="both", expand=1)

        top.update()
        tree_width = top.winfo_width()
        tree.set_columns(("test 1 dddddddddddddddddddddkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkm", "test 2", "test 3"))
        tree.set_columns_width(tree_width, (0.6, 0.2, 0.2))

    def create_options_container(self):
        options_container = tk.Frame(self)
        cbox_container, cboxs = self.create_cbox_container()
        btn_container, buttons = self.create_btn_container(options_container)

    def create_cbox_container(self, top):
        cbox_container = tk.Frame(top)
        fuel_label = tk.Label(cbox_container)
        fuel_label.configure(text="Paliwo")
        fuel_cbox = ttk.Combobox(cbox_container)
        type_label = tk.Label(cbox_container)
        type_label.configure(text="Rodzaj pomiaru")
        type_cbox = ttk.Combobox(cbox_container)
        return cbox_container, (fuel_cbox, type_cbox)

    def create_btn_container(self, top):
        btn_container = tk.Frame(top)
        add_btn = AddButton(btn_container)
        add_btn.pack(side="left")
        edit_btn = EditButton(btn_container)
        edit_btn.pack(side="left", padx=10)
        delete_btn = DeleteButton(btn_container)
        delete_btn.pack(side="left")
        return btn_container, (add_btn, edit_btn, delete_btn)

    def create_list_container(self):
        list_container = tk.Frame(self)
        tree = TreeList(list_container)
        tree.pack(fill="both", expand=1)
        return list_container, tree
