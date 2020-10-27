from .templates.config_calculation_frame import ConfigCalculationFrameTemplate
from ...globals import INTEGRATION_METHODS


class ConfigEngineParametersFrame(ConfigCalculationFrameTemplate):
    INPUT_VARIABLES = (("Średnica wylotowa\ndyszy [mm]", "Ciśnienie zewnętrzne\n[hPa]"),
                       ("Impuls jednostkowy\n[kN*s/kg]", "Przyspieszenie\nziemskie [m/s2]"),
                       )

    CBOX_VARIABLES = (
    {"Metoda całkowania": tuple(INTEGRATION_METHODS.keys())}, 
    )

    TITLE = "WYZNACZANIE WSPÓŁCZYNNIKÓW STRAT GAZODYNAMICZNYCH I CIEPLNYCH"
