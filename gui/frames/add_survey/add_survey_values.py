from gui.frames.base import BaseFrame


class AddSurveyValuesBaseFrame(BaseFrame):
    def __init__(self, top):
        super().__init__(top)
        self.create_head_section()

    def create_head_section(self):
        title = self.create_title("IMPORTOWANIE WARTOŚCI UZYSKANYCH Z POMIARU")
        title.pack(side="top", fill="x")

    def create_body_section(self):
        pass


class AddSurveyPressureValuesFrame(AddSurveyValuesBaseFrame):
    def __init__(self, top):
        super().__init__(top)


class AddSurveyThrustValuesFrame(AddSurveyValuesBaseFrame):
    def __init__(self, top):
        super().__init__(top)


class AddSurveyDoubleValuesFrame(AddSurveyValuesBaseFrame):
    def __init__(self, top):
        super().__init__(top)