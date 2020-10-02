import tkinter as tk
import tkinter.ttk as ttk
from ..elements import TreeList
import .head.database as db
from ...globals import SURVEY_TYPES
from .templates import ListFrameTemplate


class SurveysListFrame(ListFrameTemplate):
    def __init__(self, top):
        super().__init__(top)
        self.data = []
        self.fuel_name: str
        self.survey_type: str

    def create_head_section(self, top):
        title = self.create_title(self, "LISTA POMIARÓW")
        option_container = tk.Frame(self)
        cboxs_container, self.cboxes =\
            self.create_cboxes_container(option_container)
        btns_container, self.buttons =\
            self.create_btns_container(option_container)
        cboxs_container.pack(side="left")
        btns_container.pack(side="right", padx=15)

        self.buttons[0].configure(command=lambda: top.change_frame(3))
        self.cboxes[0].configure(values=db.get_fuels_list())
        self.cboxes[1].configure(values=tuple(SURVEY_TYPES.keys()))
        for cbox in self.cboxes:
            cbox.configure(state='readonly')
            cbox.bind("<<ComboboxSelected>>", self.refresh_list)

        title.pack(side="top", fill="x")
        option_container.pack(side="top", fill="both")

    def create_body_section(self, top):
        self.tree_list = TreeList(self)
        comment_container, self.comment_elements =\
            self.create_comment_container(self)

        self.tree_list.pack(fill="both", expand=1)
        comment_container.pack(side="bottom", fill="x")

        columns = {"Lp.": 0,
                   "Śr. kryt. dyszy [mm]": 0.25,
                   "Czas próbkowania [ms]": 0.25,
                   "Masa paliwa [g]": 0.25,
                   "Data dodania": 0.25}

        self.set_list(top, self.tree_list, columns)

    def refresh_list(self, event):
        self.fuel_name = self.cboxes[0].get()
        self.survey_type = self.cboxes[1].get()
        if self.survey_type and self.fuel_name:
            self.data = self.load_data()
        self.reload_list()

    def load_data(self):
        return db.load_surveys(
            self.fuel_name, SURVEY_TYPES[self.survey_type])

    @staticmethod
    def fill_list(tree_frame, data):
        if not data:
            return
        surveys_data = []
        for number, survey in enumerate(data):
            surveys_data.append((number+1, survey.jet_diameter, survey.sampling_time,
                                 survey.fuel_mass, survey.save_date))
        tree_frame.set_data(surveys_data)

    def reload_list(self):
        self.tree_list.clean()
        self.fill_list(self.tree_list, self.data)

    @staticmethod
    def create_cboxes_container(top):
        container = tk.Frame(top)
        left = tk.Frame(container)
        fuel_label = tk.Label(left)
        fuel_label.configure(text="Paliwo")
        fuel_cbox = ttk.Combobox(left)

        right = tk.Frame(container)
        type_label = tk.Label(right)
        type_label.configure(text="Rodzaj pomiaru")
        type_cbox = ttk.Combobox(right)

        fuel_label.pack(side="left")
        fuel_cbox.pack(side="left")
        type_label.pack(side="left")
        type_cbox.pack(side="left")

        left.pack(side="left")
        right.pack(side="left", padx=10)
        return container, (fuel_cbox, type_cbox)
