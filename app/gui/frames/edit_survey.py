from .add_survey import AddSurveyFrame


class EditSurveyFrame(AddSurveyFrame):
    def __init__(self, top):
        super().__init__(top)
        self.title.configure(text="EDYTOWANIE POMIARU")
        name_cbox, _ = self.get_comboboxes()
        name_cbox.configure(state="disabled")
        self.survey = None
        self.survey_id = None

    def set_values(self, values):
        self.clean()
        name_cbox, survey_type_cbox = self.get_comboboxes()
        sampling_time = self.init_widgets[1]

        name_cbox.set(values[0])
        survey_type_cbox.set(values[1])
        sampling_time.insert('0', values[2])

        fields = self.survey_table.fields + self.fuel_table.fields
        for field, value in zip(fields, values[3:-1]):
            field.entry.insert(0, value)

        self.comment.insert('end', values[-1].rstrip())
