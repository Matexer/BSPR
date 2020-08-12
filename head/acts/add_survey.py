from head.objects import Survey
from globals import SURVEY_TYPES


class AddSurveyAct:
    def __init__(self, top):
        self.top = top
        self.frame = top.frames[3]
        self.fuels_data = self.get_fuels_data()
        self.add_frame_btns = self.frame.get_buttons()
        self.add_frame_cboxes = self.frame.get_comboboxes()
        self.set_comboboxes()
        self.set_buttons()

    def set_comboboxes(self):
        f_name = self.frame.name_cbox
        s_type = self.frame.init_widgets[0]
        fuel_names = [fuel.name for fuel in self.fuels_data]
        f_name.configure(values=fuel_names)
        s_type.configure(values=tuple(SURVEY_TYPES.keys()))

    def get_fuels_data(self):
        fuels_list_frame = self.top.frames[0]
        fuels_data = fuels_list_frame.data
        return fuels_data

    def set_buttons(self):
        import_values_btn = self.add_frame_btns[0]
        import_values_btn.configure(command=lambda: self.import_survey_values())

        fill_fuel_data_btn = self.add_frame_btns[1]
        save_btn = self.add_frame_btns[2]

    def import_survey_values(self):
        survey_type = self.get_survey_type()
        if survey_type == "press":
            self.top.change_frame(5)
        elif survey_type == "thrust":
            self.top.change_frame(6)
        elif survey_type == "pressthru":
            self.top.change_frame(7)

    def get_survey_type(self):
        survey_type_cbox = self.add_frame_cboxes[1]
        type_name = survey_type_cbox.get()
        if type_name in SURVEY_TYPES.keys():
            s_type = SURVEY_TYPES[type_name]
            return s_type
