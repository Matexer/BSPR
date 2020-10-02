from tkinter import messagebox as mb
import head.database as db
from .template import ListActTemplate
from globals import SURVEY_TYPES


class SurveysListAct(ListActTemplate):
    def __init__(self, top):
        super().__init__(top, top.frames[2])

    def set_buttons(self, frame):
        edit_btn = frame.buttons[1]
        delete_btn = frame.buttons[2]

        edit_btn.configure(command=lambda: self.edit_survey())
        delete_btn.configure(command=lambda: self.delete_surveys())

    def edit_survey(self):
        ids = self.get_selected_surveys()
        if ids:
            db_id = self.tree_list.tree.get_children().index(ids[0])
            edit_frame = self.top.frames[8]
            survey = self.frame.data[db_id]
            values = list(survey.export().values())[:12]
            reversed_survey_types =\
                {val: key for key, val in SURVEY_TYPES.items()}
            values[0] = reversed_survey_types[values[0]]
            values = [self.frame.fuel_name] + values
            edit_frame.survey = survey
            edit_frame.survey_id = db_id
            edit_frame.set_values(values)
            self.top.change_frame(8)

    def delete_surveys(self):
        tree = self.frame.tree_list.tree
        ids = self.get_selected_surveys()
        if ids:
            chosen_s_number = len(ids)
            title = "Usunięcie pomiarów"
            message = "Czy chcesz usunąć %i " % chosen_s_number
            if chosen_s_number > 1:
                if chosen_s_number < 5:
                    message += "wybrane pomiary z bazy danych?"
                else:
                    message += "wybranych pomiarów z bazy danych?"
            else:
                title = "Usunięcie pomiaru"
                message = "Czy chcesz usunąć wybrany pomiar z bazy danych?"

            reply = mb.askyesno(title, message)
            if reply:
                for s_id in ids:
                    s_db_id = tree.get_children().index(s_id)
                    tree.selection_remove(s_id)
                    db.remove_survey(
                        self.frame.fuel_name, self.frame.data[s_db_id].type, s_db_id)
                    tree.delete(s_id)
                    self.frame.data = self.frame.load_data()

    def get_selected_surveys(self):
        return self.tree_list.tree.selection()
