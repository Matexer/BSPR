import tkinter as tk
from gui.elements import *
from gui.configure import AF_BG


class FuelsListFrame(ActionFrame):
    def __init__(self, top):
        ActionFrame.__init__(self, top)

        btn_container, self.buttons = self.create_btn_container()
        list_container, tree = self.create_list_container()

        self.buttons[0].configure(command=lambda: top.change_frame(1))

        btn_container.pack(side="top")
        list_container.pack(fill="both", expand=1)

        top.update()
        tree_width = top.winfo_width()
        tree.set_columns(("test 1 dddddddddddddddddddddkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkm", "test 2", "test 3"))
        tree.set_columns_width(tree_width, (0.6, 0.2, 0.2))

    def create_btn_container(self):
        btn_container = tk.Frame(self)
        add_btn = AddButton(btn_container)
        add_btn.pack(side="left")
        edit_btn = EditButton(btn_container)
        edit_btn.pack(side="left")
        delete_btn = DeleteButton(btn_container)
        delete_btn.pack(side="left")
        return btn_container, (add_btn, edit_btn, delete_btn)

    def create_list_container(self):
        list_container = tk.Frame(self,
                                  background="green")
        tree = TreeList(list_container)
        tree.pack(fill="both", expand=1)
        return list_container, tree
