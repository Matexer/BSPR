from ..templates import ConfigCalculationActTemplate


class ConfigAnAct(ConfigCalculationActTemplate):
    FRAME_NUMBER = 10
    NEEDED_SURVEY_TYPES = "press", "pressthru"

