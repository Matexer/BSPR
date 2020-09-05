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

        cboxes = {
                 "Metoda całkowania": ("liniowa", "trapezów", "Simpsona"),
                 "Dla wartości": ("średniej", "chwilowej")
                 }

        cboxes_container, self.cboxes_frame =\
            self.create_cbox_container(self, cboxes)

        inputs = (("K",),
                  ("Impuls jednostkowy",))

        inputs_container, self.inputs_frame =\
            self.create_input_container(self, inputs)

        cboxes_container.pack(fill="both")
        inputs_container.pack(fill="both")
        surveys_cont.pack(fill="both")

    def create_cbox_container(self, top, cboxes):
        container = tk.Frame(top)
        subtitle = self.create_subtitle(container, "KONFIGURACJA OBLICZEŃ")
        cboxes_frame = CboxTable(container, cboxes)

        subtitle.pack(fill="x")
        cboxes_frame.pack(fill="both")
        return cboxes_frame, cboxes_frame

    def create_input_container(self, top, inputs):
        container = tk.Frame(top)
        subtitle = self.create_subtitle(container, "KONFIGURACJA OBLICZEŃ")
        inputs_table_frame = InputTable(container, inputs)

        subtitle.pack(fill="x")
        inputs_table_frame.pack(fill="both")
        return container, inputs_table_frame

    def create_surveys_container(self, top, columns):
        container = tk.Frame(top)
        subtitle = self.create_subtitle(container, "LISTA DOSTĘPNYCH POMIARÓW")
        ch_list = ChooseList(container)
        ch_list.tree_frame.set_columns(list(columns.keys()))

        subtitle.pack(fill="x")
        ch_list.pack(pady=10)

        top.update()
        tree_width = top.winfo_width() // self.SURVEY_PLOT_TO_LIST_PROPORTION
        ch_list.tree_frame.set_columns_width(tree_width, tuple(columns.values()))
        return container, ch_list
