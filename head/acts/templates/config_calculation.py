from typing import List, Dict, Tuple
import head.database as db
from globals import SURVEY_TYPES

from gui.TopWindow import TopWindow
from head.objects.survey import Survey


class ConfigCalculationActTemplate:
    INPUT_VARIABLES = (("Var 1", "Var 2"),
                       ("Var 3", "Var 4"))

    CBOX_VARIABLES = (({"Set 1": ("op. 1", "op. 2", "op. 3")},
                       {"Set 2": ("op. 1", "op. 2", "op. 3")}),

                      ({"Set 3": ("op. 1", "op. 2", "op. 3")},
                       {"Set 4": ("op. 1", "op. 2", "op. 3")}))

    LIST_COLUMNS = ("ŚKD [mm]", )
    SURVEY_ARGS = ("jet_diameter", )

    FRAME_NUMBER = 9
    NEEDED_SURVEY_TYPES = tuple(SURVEY_TYPES.values())[:2]

    def __init__(self, top: TopWindow):
        self.top = top
        self.frame = top.frames[self.FRAME_NUMBER]

        self.surveys = Dict[str, Tuple[Survey]]
        self.activate_events()

    def activate_events(self):
        self.frame.ch_fuel_cbox.bind(
            "<<ComboboxSelected>>", lambda e: self.__load_surveys())

    def __load_surveys(self):
        fuel_name = self.frame.ch_fuel_cbox.get()
        for survey_type in self.NEEDED_SURVEY_TYPES:
            self.surveys.update(
                {survey_type: self.__load_surveys_from_db(
                    fuel_name, survey_type)})

        if any(self.surveys.values() != False):
            self.set_surveys_list()

    def set_surveys_list(self):
        list_data = []
        plots_data = []
        NESTED = False
        for survey_type in self.surveys.keys():
            if survey_type == tuple(SURVEY_TYPES.keys()[0]):
                NESTED = True
            else:
                NESTED = False

            for survey in self.surveys[survey_type]:
                list_data.append(
                    [survey.__getattribute__(arg) for arg in self.SURVEY_ARGS])

                vals = survey.values[0] if NESTED else survey.values
                plots_data.append((vals,
                                   survey.sampling_time,
                                   survey.comment))

        self.frame.surveys_list.tree_frame.set_data(list_data)
        self.frame.surveys_list.set_plots_data(plots_data)

    @staticmethod
    def __load_surveys_from_db(
            fuel_name: str, survey_type: SURVEY_TYPES.values())\
            -> List[Survey] or False:
        return db.load_surveys(fuel_name, survey_type)
