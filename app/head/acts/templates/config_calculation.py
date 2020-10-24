from typing import List, Optional, Iterable
from ....head.database import Database as db
from ....globals import SURVEY_TYPES
from ....head.data_management import DataManager as Dm
from ....head.messages import Messages as Msg
from ....gui.TopWindow import TopWindow
from ....head.objects.survey import Survey


class ConfigCalculationActTemplate:
    LIST_COLUMNS = "ŚKD [mm]",
    SURVEY_ARGS = "jet_diameter",

    FRAME_NUMBER = 9
    OUTPUT_FRAME_NUMBER = 12
    NEEDED_SURVEY_TYPES = "press", "pressthru"

    def __init__(self, top: TopWindow):
        self.top = top
        self.frame = top.frames[self.FRAME_NUMBER]
        self.surveys = {}

        self.frame.ch_fuel_cbox.bind(
            "<Button>", lambda e: self.__set_fuels_cbox())

        self.activate_events()
        self.set_buttons()

    def activate_events(self):
        self.frame.ch_fuel_cbox.bind(
            "<<ComboboxSelected>>", lambda e: self.__load_surveys())

    def set_buttons(self):
        self.frame.navi_buttons[0].configure(
            command=lambda: self.start())
        self.frame.navi_buttons[1].configure(
            command=lambda: self.clean())

    def start(self):
        data = self.parse_data()
        if data:
            self.start_calculation(data)

    def start_calculation(self, data):
        "To be overwritten by the child class."
        pass

    def parse_data(self):
        message = self.frame.show_message

        fuel_name = self.frame.ch_fuel_cbox.get()
        if not fuel_name:
            message(Msg.needs_to_choose_fuel)
            return

        inputs, report = self.valid_inputs(self.get_values_from_inputs())
        self.point_mistakes(report)
        if report:
            message(self.get_msg_from_report(report))
            return

        cboxes, invalid_fields = self.get_valid_values_from_cboxes()
        if invalid_fields:
            message(Msg.needs_to_fulfil_field(invalid_fields[0]))
            return

        surveys = self.get_chosen_surveys()
        survey_issue = self.check_surveys(surveys)
        if survey_issue:
            message(survey_issue)
            return

        times = self.get_times()

        self.frame.hide_message()
        return fuel_name, cboxes, inputs, surveys, times

    def get_values_from_inputs(self):
        if self.frame.inputs_frame:
            return self.frame.inputs_frame.get_inserted_values()

    def get_valid_values_from_cboxes(self):
        if self.frame.cboxes_frame:
            return self.frame.cboxes_frame.get_validated_values()

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

    def valid_inputs(self, inputs):
        values, report = Dm.to_float(inputs)
        if report:
            return values, report

        if inputs:
            names = tuple(self.flatten_nested_list(self.frame.INPUT_VARIABLES))
            report = Dm.are_bigger_than_0(values, names)
        return values, report

    @staticmethod
    def check_surveys(surveys):
        jets = set(s.jet_diameter for s in surveys)
        if len(jets) < 2:
            return Msg.needs_2_diff_jets_diam

    def point_mistakes(self, report):
        if self.frame.inputs_frame:
            self.frame.inputs_frame.point_entries(report)

    @staticmethod
    def get_msg_from_report(report):
        for point in report:
            if point:
                return point

    def flatten_nested_list(self, nested):
        for item in nested:
            if isinstance(item, Iterable) and not isinstance(item, str):
                for val in self.flatten_nested_list(item):
                    yield val
            else:
                yield item

    def clean(self):
        self.frame.ch_fuel_cbox.set('')
        if self.frame.inputs_frame:
            self.frame.inputs_frame.clean()
        if self.frame.cboxes_frame:
            self.frame.cboxes_frame.clean()
        self.frame.surveys_list.clean()
        self.frame.hide_message()

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
