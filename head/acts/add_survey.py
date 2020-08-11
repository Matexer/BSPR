from head.objects import Survey
from globals import SURVEY_TYPES


class AddSurveyAct:
    def __init__(self, top):
        self.top = top
        self.frame = top.frames[3]
        self.fuels_data = self.get_fuels_data()
        self.set_comboboxes()

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
