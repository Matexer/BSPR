from ..add_survey import AddSurveyValuesAct


class EditSurveyValuesAct(AddSurveyValuesAct):
    def __init__(self, top, import_frame, survey):
        super().__init__(top, import_frame, survey)
        self.previous_frame_number = 8
