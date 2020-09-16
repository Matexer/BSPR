import tkinter as tk
import tkinter.ttk as ttk
from .scrolled_frame import ScrolledFrameTemplate
from gui.elements import ChooseList, CboxTable, InputTable
from head.objects.fuel import Fuel


class ConfigCalculationFrameTemplate(ScrolledFrameTemplate):
    SURVEY_PLOT_TO_LIST_PROPORTION = 3

    def __init__(self, top, *args, **kwargs):
        super().__init__(top, *args, **kwargs)
        self.cboxes_frame: CboxTable(tk.Frame, tuple)
        self.inputs_frame: InputTable(tk.Frame, tuple)
        self.surveys_list: ChooseList(tk.Frame, *args, **kwargs)
        self.surveys: list
        self.chosen_fuel: Fuel

        self.test()

    @staticmethod
    def create_choose_fuel_container(top):
        container = tk.Frame(top)
        tk.Label(container, text="Dla paliwa").pack(side="left")
        cbox = ttk.Combobox(container, state="readonly", width=30)
        cbox.pack(side="left", padx=10)
        return container, cbox

    def create_cbox_container(self, top, cboxes):
        container = tk.Frame(top)
        subtitle = self.create_subtitle(container, "KONFIGURACJA OBLICZEŃ")
        cboxes_frame = CboxTable(container, cboxes)

        subtitle.pack(fill="x")
        cboxes_frame.pack(fill="both")
        return container, cboxes_frame

    def create_inputs_container(self, top, inputs):
        container = tk.Frame(top)
        subtitle = self.create_subtitle(container, "WARTOŚCI ZMIENNYCH")
        inputs_table_frame = InputTable(container, inputs)

        subtitle.pack(fill="x")
        inputs_table_frame.pack(fill="both")
        return container, inputs_table_frame

    def create_surveys_container(self, top, columns):
        container = tk.Frame(top)
        subtitle = self.create_subtitle(container, "LISTA DOSTĘPNYCH POMIARÓW")
        ch_list = ChooseList(container)
        ch_list.tree_frame.set_columns(tuple(columns.keys()))

        subtitle.pack(fill="x")
        ch_list.pack(pady=10)

        top.update()
        tree_width = top.winfo_width() // self.SURVEY_PLOT_TO_LIST_PROPORTION
        ch_list.tree_frame.set_columns_width(tree_width, tuple(columns.values()))
        return container, ch_list

    def create_down_nav_container(self, top):
        container, btns = super().create_down_nav_container(top)
        btns[0].config(text="DALEJ")
        btns[2].pack_forget()
        return container, btns

    def test(self):
        title = self.create_title(self.interior, "WYZNACZANIE IMPULSU JEDNOSTKOWEGO")

        ch_fuel_container, self.ch_fuel_cbox =\
            self.create_choose_fuel_container(self.interior)

        columns = {"ŚKD": 0.5}
        surveys_cont, self.surveys_list =\
            self.create_surveys_container(self.interior, columns)

        self.surveys_list.tree_frame.set_data(((1, 2), (3, 4)))
        plots_data = (((1, 2, 4), 5, "egg"), ((4, 5, 4), 2, "milk"))
        self.surveys_list.set_plots_data(plots_data)

        cboxes = ({
                 "Metoda całkowania": ("liniowa", "trapezów", "Simpsona")},

                  {"Dla wartości": ("średniej", "chwilowej")
                  })

        cboxes_container, self.cboxes_frame =\
            self.create_cbox_container(self.interior, cboxes)

        inputs = (("K",),
                  ("Impuls jednostkowy",))

        inputs_container, self.inputs_frame =\
            self.create_inputs_container(self.interior, inputs)

        navi_container, self.navi_buttons = self.create_down_nav_container(self)

        title.pack(fill="x")
        ch_fuel_container.pack(fill="both", pady=10)
        inputs_container.pack(fill="both")
        cboxes_container.pack(fill="both")
        surveys_cont.pack(fill="both")
        navi_container.pack(side="bottom", fill="x")
