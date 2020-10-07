from ..templates import ConfigCalculationActTemplate
from ....core import Data, Config
from ..calculation import AnAct
from ....globals import INTEGRATION_METHODS, CALCULATION_METHODS


class ConfigAnAct(ConfigCalculationActTemplate):
    FRAME_NUMBER = 10
    NEEDED_SURVEY_TYPES = "press", "pressthru"

    def start_calculation(self, data):
        fuel_name, cboxes, variables, surveys, times =\
             data

        data = Data(surveys, times, variables)
        config = Config(CALCULATION_METHODS[cboxes[0]],
            INTEGRATION_METHODS[cboxes[1]])
        AnAct(self.top, fuel_name, data, config)
        self.top.change_frame(self.OUTPUT_FRAME_NUMBER)
