from typing import List, Optional
import head.database as db
from globals import SURVEY_TYPES
from head.data_management import DataManager as Dm
from head.messages import Messages as Msg

from gui.TopWindow import TopWindow
from head.objects.survey import Survey


class ConfigCalculationActTemplate:
    INPUT_VARIABLES = (("Var 1", "Var 2"),
                       ("Var 3", "Var 4"))

    CBOX_VARIABLES = (({"Set 1": ("op. 1", "op. 2", "op. 3")},
                       {"Set 2": ("op. 1", "op. 2", "op. 3")}),

                      ({"Set 3": ("op. 1", "op. 2", "op. 3")},
                       {"Set 4": ("op. 1", "op. 2", "op. 3")}))

    LIST_COLUMNS = "ŚKD [mm]",
    SURVEY_ARGS = "jet_diameter",

    FRAME_NUMBER = 9
    NEEDED_SURVEY_TYPES = "press", "pressthru"

    def __init__(self, top: TopWindow):
        self.top = top
        self.frame = top.frames[self.FRAME_NUMBER]
        self.surveys = {}

        self.__set_fuels_cbox()
        self.activate_events()
        self.set_buttons()

    def activate_events(self):
        self.frame.ch_fuel_cbox.bind(
            "<<ComboboxSelected>>", lambda e: self.__load_surveys())

    def set_buttons(self):
        self.frame.navi_buttons[0].configure(command=lambda: self.parse_data())
        self.frame.navi_buttons[1].configure(command=lambda: self.clean())

    def parse_data(self):
        message = self.frame.show_message

        fuel_name = self.frame.ch_fuel_cbox.get()
        if not fuel_name:
            message(Msg.needs_to_choose_fuel)
            return

        inputs, report = self.valid_inputs(self.get_values_from_inputs())
        if report:
            self.point_mistakes(report)
            message(self.get_error_msg_from_report(report))
            return

        print(self.get_values_from_cboxes())
        print(self.get_chosen_surveys())
        print(self.get_times())

    def get_values_from_inputs(self):
        return self.frame.inputs_frame.get_inserted_values()

    def get_values_from_cboxes(self):
        return self.frame.cboxes_frame.get_inserted_values()

    def get_chosen_surveys(self):
        ids = tuple(self.frame.surveys_list.tree_frame.get_chosen_ids())
        surveys_list = tuple(*filter(lambda x: x, self.surveys.values()))
        return [surveys_list[i] for i in ids]

    def get_times(self):
        ids = tuple(self.frame.surveys_list.tree_frame.get_chosen_ids())
        lines = self.frame.surveys_list.surveys_t_lines
        selected_lines = (lines[i] for i in ids)
        x_values = (line.get_xdata() for line in selected_lines)
        parse_val = lambda x: x[0] if isinstance(x, (list, tuple)) else x
        return list(map(parse_val, x_values))

    @staticmethod
    def valid_inputs(inputs):
        return Dm.to_float(inputs)

    @staticmethod
    def valid_cboxes(cboxes):
        if all(cboxes):
            return cboxes, False

        report = []
        for value in cboxes:
            if value:




    def point_mistakes(self, report):
        self.frame.inputs_frame.point_entries(report)

    @staticmethod
    def get_error_msg_from_report(report):
        for point in report:
            if point:
                return point

    def clean(self):
        self.frame.ch_fuel_cbox.set('')
        self.frame.inputs_frame.clean()
        self.frame.cboxes_frame.clean()
        self.frame.surveys_list.clean()

    def __set_fuels_cbox(self):
        fuels = db.get_fuels_list()
        self.frame.ch_fuel_cbox.config(values=fuels)

    def __load_surveys(self):
        fuel_name = self.frame.ch_fuel_cbox.get()
        if not fuel_name:
            return
        for survey_type in self.NEEDED_SURVEY_TYPES:
            self.surveys.update(
                {survey_type: self.__load_surveys_from_db(
                    fuel_name, survey_type)})

        self.frame.surveys_list.hide_lines()
        self.__set_surveys_list()

    def __set_surveys_list(self):
        list_data = []
        plots_data = []
        for survey_type in self.surveys.keys():
            if not self.surveys[survey_type]:
                continue

            for survey in self.surveys[survey_type]:
                list_data.append(
                    [survey.__getattribute__(arg) for arg in self.SURVEY_ARGS])

                plots_data.append((survey.values[0],
                                   survey.sampling_time,
                                   survey.comment))

        self.frame.surveys_list.tree_frame.set_data(list_data)
        self.frame.surveys_list.set_plots_data(plots_data)

    @staticmethod
    def __load_surveys_from_db(
            fuel_name: str, survey_type: SURVEY_TYPES.values())\
            -> Optional[List[Survey]]:
        return db.load_surveys(fuel_name, survey_type)
