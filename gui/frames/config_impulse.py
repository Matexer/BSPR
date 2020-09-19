from .templates.config_calculation_frame import ConfigCalculationFrameTemplate


class ConfigImpulseFrame(ConfigCalculationFrameTemplate):
    INPUT_VARIABLES = False

    SURVEY_LIST_COLUMNS = {"ŚKD": 0.34, "k": 0.34}

    TITLE = "WYZNACZANIE IMPULSU JEDNOSTKOWEGO"

    def __init__(self, top):
        super().__init__(top)
