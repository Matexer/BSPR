from .templates.config_calculation_frame import ConfigCalculationFrameTemplate


class ConfigEngineParametersFrame(ConfigCalculationFrameTemplate):
    INPUT_VARIABLES = (("Fw", "Xa"),
                       ("zeta", "Impuls jednostkowy"),
                       ("Ciśnienie zewnętrzne", )
                       )

    TITLE = "WYZNACZANIE WSPÓŁCZYNNIKÓW STRAT GAZODYNAMICZNYCH I CIEPLNYCH"

    def __init__(self, top):
        super().__init__(top)
