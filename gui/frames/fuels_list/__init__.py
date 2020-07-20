import tkinter as tk
from gui.elements import AddButton, DeleteButton, EditButton
from gui.configure import AF_BG


class FuelsListFrame(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)
        self.configure(background=AF_BG)

        btn_container, self.buttons = self.create_btn_container()
        list_container = self.create_list_container()
        btn_container.pack(side="top")
        list_container.pack(fill="both", expand=1)

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
        return list_container
