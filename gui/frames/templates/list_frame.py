import tkinter as tk
from abc import ABCMeta, abstractmethod
from .frame import TemplateFrame
from gui.elements import AddButton, EditButton, DeleteButton


class ListFrameTemplate(TemplateFrame, metaclass=ABCMeta):
    def __init__(self, top):
        super().__init__(top)
        self.top = top
        self.create_head_section(self)
        self.create_body_section(self)

    @abstractmethod
    def create_head_section(self, top):
        pass

    @abstractmethod
    def create_body_section(self, top):
        pass

    @staticmethod
    def create_btns_container(top):
        container = tk.Frame(top)
        add_btn = AddButton(container)
        add_btn.pack(side="left")
        edit_btn = EditButton(container)
        edit_btn.pack(side="left", padx=10)
        delete_btn = DeleteButton(container)
        delete_btn.pack(side="left")
        return container, (add_btn, edit_btn, delete_btn)

    @staticmethod
    def create_comment_container(top):
        container = tk.Frame(top)
        left_cont = tk.Frame(container)
        tk.Label(left_cont,
                 text="Data dodania:",
                 font="bold").pack(anchor="w")
        adding_date = tk.Label(left_cont)
        adding_date.pack(anchor="w")
        tk.Label(left_cont,
                 text="Ostatnia modyfikacja:",
                 font="bold").pack(anchor="w")
        modify_date = tk.Label(left_cont)
        modify_date.pack(anchor="w")

        right_cont = tk.Frame(container)
        tk.Label(right_cont,
                 text="Komentarz:",
                 font="bold").pack(anchor="w")
        comment = tk.Label(right_cont, anchor='w', justify="left")
        comment.pack(anchor="w")

        left_cont.pack(side="left", anchor="n")
        right_cont.pack(side="left", anchor="n", padx=15)
        return container, (adding_date, modify_date, comment)

    @staticmethod
    def set_list(top, tree, columns):
        top.update()
        tree_width = top.winfo_width()
        tree.set_columns(list(columns.keys()))
        tree.set_columns_width(tree_width, list(columns.values()))
