from .templates.config_calculation_frame import ConfigCalculationFrameTemplate


class ConfigEngineParametersFrame(ConfigCalculationFrameTemplate):
    INPUT_VARIABLES = (("Fw", "Xa"),
                       ("zeta",),
                       ("Ciśnienie zewnętrzne", "Impuls jednostkowy")
                       )

    TITLE = "WYZNACZANIE WSPÓŁCZYNNIKÓW STRAT GAZODYNAMICZNYCH I CIEPLNYCH"
