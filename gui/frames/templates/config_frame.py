import tkinter as tk
from .frame import FrameTemplate
from gui.elements import ChooseList, CboxTable, InputTable


class ConfigFrameTemplate(FrameTemplate):
    SURVEY_PLOT_TO_LIST_PROPORTION = 3

    def __init__(self, top, *args, **kwargs):
        super().__init__(top, *args, **kwargs)

        columns = {"Lp.": 0.3, "ŚKD": 0.3}
        surveys_cont, self.surveys_list =\
            self.create_surveys_container(self, columns)

        surveys_cont.pack(fill="both")

    def create_cbox_container(self, top):
        subtitle = self.create_subtitle(self, "KONFIGURACJA OBLICZEŃ")

    def create_surveys_container(self, top, columns):
        container = tk.Frame(self)
        subtitle = self.create_subtitle(self, "LISTA DOSTĘPNYCH POMIARÓW")
        ch_list = ChooseList(container)
        ch_list.tree_frame.set_columns(list(columns.keys()))

        subtitle.pack(fill="x")
        ch_list.pack(pady=10)

        top.update()
        tree_width = top.winfo_width() // self.SURVEY_PLOT_TO_LIST_PROPORTION
        ch_list.tree_frame.set_columns_width(tree_width, tuple(columns.values()))
        return container, ch_list
