from ..templates import ConfigCalculationActTemplate
from ...messages import Messages as Msg


class ConfigImpulseAct(ConfigCalculationActTemplate):
    FRAME_NUMBER = 9
    NEEDED_SURVEY_TYPES = "press", "pressthru"
    
    @staticmethod
    def check_surveys(surveys):
        if not surveys:
            return Msg.needs_min_one_survey
