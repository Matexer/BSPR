from ..templates import ConfigCalculationActTemplate


class ConfigImpulseAct(ConfigCalculationActTemplate):
    FRAME_NUMBER = 9
    NEEDED_SURVEY_TYPES = "press", "pressthru"
