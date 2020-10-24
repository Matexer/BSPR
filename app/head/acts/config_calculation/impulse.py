from ..templates import ConfigCalculationActTemplate
from ...messages import Messages as Msg
from ....core import Data, Config
from ..calculation import ImpulseAct
from ....globals import INTEGRATION_METHODS


class ConfigImpulseAct(ConfigCalculationActTemplate):
    FRAME_NUMBER = 9
    NEEDED_SURVEY_TYPES = "thrust", "pressthru"
    SHOW_VALUES = "thrust"


    @staticmethod
    def check_surveys(surveys):
        if not surveys:
            return Msg.needs_min_one_survey

    def start_calculation(self, data):
        fuel_name, cboxes, _, surveys, _ =\
             data

        data = Data(surveys)
        config = Config(INTEGRATION_METHODS[cboxes[0]])
        ImpulseAct(self.top, fuel_name, data, config)
        self.top.change_frame(self.OUTPUT_FRAME_NUMBER)
