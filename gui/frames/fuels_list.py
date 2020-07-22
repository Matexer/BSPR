import tkinter as tk
from gui.elements import *
from gui.configure import AF_BG


class FuelsListFrame(ActionFrame):
    def __init__(self, top):
        ActionFrame.__init__(self, top)

        btn_container = tk.Frame(self)
        list_container = tk.Frame(self)
        self.buttons = self.create_btns(btn_container)
        tree = self.create_list(list_container)

        self.buttons[0].configure(command=lambda: top.change_frame(1))

        btn_container.pack(side="top", pady=5)
        list_container.pack(fill="both", expand=1)

        top.update()
        tree_width = top.winfo_width()
        tree.set_columns(("test 1 dddddddddddddddddddddkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkm", "test 2", "test 3"))
        tree.set_columns_width(tree_width, (0.6, 0.2, 0.2))

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
