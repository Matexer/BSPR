from .templates.config_calculation_frame import ConfigCalculationFrameTemplate


class ConfigAnFrame(ConfigCalculationFrameTemplate):
    INPUT_VARIABLES = ("Zakładane prędkości maksymalne gazów [m/s]", )

    TITLE = "WYZNACZANIE WSPÓŁCZYNNIKÓW A i n PRAWA SZYBKOŚCI SPALANIA"
