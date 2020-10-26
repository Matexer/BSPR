from typing import NamedTuple
from ...objects import Fuel
from ...database import Database as db
from ..templates import ConfigCalculationActTemplate
from ....core import Data, Config
from ..calculation import AnAct
from ....globals import INTEGRATION_METHODS, CALCULATION_METHODS


class AnVariables(NamedTuple):
    w: float
    fuel: Fuel


class ConfigAnAct(ConfigCalculationActTemplate):
    FRAME_NUMBER = 10
    NEEDED_SURVEY_TYPES = "press", "pressthru"

    def start_calculation(self, data):
        fuel_name, cboxes, variables, surveys, times =\
             data

        fuel = db.load_fuel(fuel_name)
        An_variables = AnVariables(variables[0], fuel)
        data = Data(surveys, times, An_variables)
        config = Config(INTEGRATION_METHODS[cboxes[1]],
            CALCULATION_METHODS[cboxes[0]])
        AnAct(self.top, fuel_name, data, config)
        self.top.change_frame(self.OUTPUT_FRAME_NUMBER)
