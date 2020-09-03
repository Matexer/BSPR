import tkinter as tk
from .frame import FrameTemplate
from gui.elements import ChooseList, CboxTable, InputTable


class ConfigFrameTemplate(FrameTemplate):
    def __init__(self, top, *args, **kwargs):
        super().__init__(top, *args, **kwargs)
        sur_cont = self.create_surveys_container(top, 1)
        sur_cont.pack()

    def create_config_table_container(self, top):
        pass

    def create_surveys_container(self, top, surveys):
        container = tk.Frame(self)
        ch_list = ChooseList(container)
        ch_list.set_columns(("Lp.", "ŚKD", "k"))
        ch_list.pack()

        top.update()
        tree_width = top.winfo_width() // 3
        ch_list.set_columns_width(tree_width, (0.3, 0.3, 0.3))
        return container
