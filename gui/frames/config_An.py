from .templates.config_calculation_frame import ConfigCalculationFrameTemplate


class ConfigAnFrame(ConfigCalculationFrameTemplate):
    INPUT_VARIABLES = ("Zakładane prędkości maksymalne gazów", )

    TITLE = "WYZNACZANIE WSPÓŁCZYNNIKÓW A i n PRAWA SZYBKOŚCI SPALANIA"

    def __init__(self, top):
        super().__init__(top)
