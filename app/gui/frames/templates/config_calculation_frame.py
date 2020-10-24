import tkinter as tk
import tkinter.ttk as ttk
from .scrolled_frame import ScrolledFrameTemplate
from ...elements import ChooseList, CboxTable, InputTable
from ....head.objects import Fuel
from ....head.database import Database as db
from ....globals import INTEGRATION_METHODS, CALCULATION_METHODS


class ConfigCalculationFrameTemplate(ScrolledFrameTemplate):
    SURVEY_PLOT_TO_LIST_PROPORTION = 3

    INPUT_VARIABLES = (("Var 1", "Var 2"),
                       ("Var 3", "Var 4"))

    CBOX_VARIABLES = (
        {"Dla wartości": tuple(CALCULATION_METHODS.keys())},
        {"Metoda całkowania": tuple(INTEGRATION_METHODS.keys())}
    )

    SURVEY_LIST_COLUMNS = {"ŚKD": 0.5}

    TITLE = "ConfigCalculationFrameTemplate"

    def __init__(self, top, *args, **kwargs):
        super().__init__(top, *args, **kwargs)
        self.cboxes_frame: CboxTable(tk.Frame, tuple)
        self.inputs_frame: InputTable(tk.Frame, tuple)
        self.surveys_list: ChooseList(tk.Frame, *args, **kwargs)
        self.surveys: list
        self.chosen_fuel: Fuel

        self.inputs_frame = None
        self.cboxes_frame = None

        self.generate_structure()
        self.set_plot_labels(self.surveys_list.plot_frame.plot)

    @staticmethod
    def set_plot_labels(plot):
        plot.set_title("Wykres/y pomiaru ciśnienia od czasu")
        plot.set_xlabel("Czas [ms]")
        plot.set_ylabel("Ciśnienie [MPa]")

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
        ch_list.plot_frame.fig.subplots_adjust(
            left=0.09, bottom=0.105, right=0.983, top=0.933)

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

    def generate_structure(self):
        title = self.create_title(
            self.interior, self.TITLE)

        ch_fuel_container, self.ch_fuel_cbox =\
            self.create_choose_fuel_container(self.interior)

        columns = {"ŚKD": 0.5}
        surveys_cont, self.surveys_list =\
            self.create_surveys_container(self.interior, columns)

        if self.CBOX_VARIABLES:
            cboxes_container, self.cboxes_frame =\
                self.create_cbox_container(self.interior, self.CBOX_VARIABLES)

        if self.INPUT_VARIABLES:
            inputs_container, self.inputs_frame =\
                self.create_inputs_container(self.interior, self.INPUT_VARIABLES)

        navi_container, self.navi_buttons =\
            self.create_down_nav_container(self)

        title.pack(fill="x")
        ch_fuel_container.pack(fill="both", pady=10)
        if self.INPUT_VARIABLES:
            inputs_container.pack(fill="both")
        if self.CBOX_VARIABLES:
            cboxes_container.pack(fill="both")
        surveys_cont.pack(fill="both")
        navi_container.pack(side="bottom", fill="x")
