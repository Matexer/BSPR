from .templates.config_calculation_frame import ConfigCalculationFrameTemplate
from ...globals import INTEGRATION_METHODS

class ConfigImpulseFrame(ConfigCalculationFrameTemplate):
    INPUT_VARIABLES = False

    CBOX_VARIABLES = (
        {"Metoda całkowania": tuple(INTEGRATION_METHODS.keys())}
    )

    SURVEY_LIST_COLUMNS = {"ŚKD": 0.34, "k": 0.34}

    TITLE = "WYZNACZANIE IMPULSU JEDNOSTKOWEGO"
