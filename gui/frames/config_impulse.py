from .templates.config_calculation_frame import ConfigCalculationFrameTemplate


class ConfigImpulseFrame(ConfigCalculationFrameTemplate):
    INPUT_VARIABLES = False

    CBOX_VARIABLES = (
        {"Metoda całkowania": ("liniowa", "trapezów", "Simpsona")}
    )

    SURVEY_LIST_COLUMNS = {"ŚKD": 0.34, "k": 0.34}

    TITLE = "WYZNACZANIE IMPULSU JEDNOSTKOWEGO"
