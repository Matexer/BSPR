from head.acts.add_survey import AddSurveyAct
from .edit_values import EditSurveyValuesAct
from gui.configure import IMP_VALUES_BTN_COLOR_2
import head.database as db

class EditSurveyAct(AddSurveyAct):
    def __init__(self, top):
        super().__init__(top)
        imp_val_btn = self.top.frames[8].get_buttons()[0]
        modify_val_btn = self.top.frames[8].get_buttons()[5]
        imp_val_btn.config(
            text="Importuj inny plik",
            background=IMP_VALUES_BTN_COLOR_2)
        modify_val_btn.configure(command=lambda: self.start_adding_act())
        modify_val_btn.pack(side="left", padx=10, pady=5)

    def set_frame(self, top):
        self.frame = top.frames[8]

    def start_adding_act(self):
        if not self.survey.values:
            self.survey = self.frame.survey
        self.change_frame(self.survey.type)
        EditSurveyValuesAct(self.top, self.import_frame, self.survey)

    def save_survey(self):
        if not self.survey.values:
            self.survey = self.frame.survey
        super().save_survey()
        self.top.change_frame(2)

    def change_buttons(self):
        pass

    def add_survey_to_database(self, values):
        f_name = values[0]
        self.survey.update(
            [self.survey.type, self.survey.sampling_time] + values[1:])
        db.edit_survey(f_name, self.frame.survey.type,
                       self.frame.survey_id, self.survey)
