import tkinter as tk
from gui.elements import *
from .template import TemplateFrame
from head.database import get_fuels_list, load_fuel


class FuelsListFrame(TemplateFrame):
    def __init__(self, top):
        TemplateFrame.__init__(self, top)
        self.top = top

        title = self.create_title("LISTA PALIW")
        btn_container = tk.Frame(self)
        list_container = tk.Frame(self)
        self.buttons = self.create_btns(btn_container)
        tree = self.create_list(list_container)

        self.buttons[0].configure(command=lambda: top.change_frame(1))

        title.pack(side="top", fill="x", anchor="w")
        btn_container.pack(side="top", pady=5)
        list_container.pack(fill="both", expand=1)

        self.tree = tree
        self.set_list()

    @staticmethod
    def create_btns(top):
        add_btn = AddButton(top)
        add_btn.pack(side="left")
        edit_btn = EditButton(top)
        edit_btn.pack(side="left", padx=10)
        delete_btn = DeleteButton(top)
        delete_btn.pack(side="left")
        return add_btn, edit_btn, delete_btn

    @staticmethod
    def create_list(top):
        tree = TreeList(top)
        tree.pack(fill="both", expand=1)
        return tree

    def set_list(self):
        tree = self.tree
        top = self.top
        top.update()
        tree_width = top.winfo_width()
        tree.set_columns(("Nazwa",
                          "Siła [MJ/kg]",
                          "k",
                          "Masa [g]",
                          "Długość [mm]",
                          "Śr. zew. [mm]",
                          "Śr. wew. [mm]"))
        tree.set_columns_width(tree_width, (0.3, 0.15, 0.07, 0.12, 0.12, 0.12, 0.12))

    def load_list_data(self):
        fuels = get_fuels_list()
        data = []
        for fuel in fuels:
            info = load_fuel(fuel)
            data.append(info)
