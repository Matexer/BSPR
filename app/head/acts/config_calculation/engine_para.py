from typing import NamedTuple
from ...messages import Messages as Msg
from ....globals import INTEGRATION_METHODS
from ..templates import ConfigCalculationActTemplate
from ...database import Database as db
from ....core import Data, Config
from ...objects import Fuel
from ...acts.calculation import EngineParaAct


class EngineParaVariables(NamedTuple):
    fuel: Fuel
    da: float #mm
    pz: float #hPa
    I1: float #kN*s/kg
    g: float #m/s2


class ConfigEngineParaAct(ConfigCalculationActTemplate):
    FRAME_NUMBER = 11
    NEEDED_SURVEY_TYPES = "pressthru",

    def start_calculation(self, data):
        fuel_name, cboxes, variables, surveys, times =\
             data

        fuel = db.load_fuel(fuel_name)
        An_variables = EngineParaVariables(fuel, *variables)
        data = Data(surveys, times, An_variables)
        config = Config(INTEGRATION_METHODS[cboxes[0]])
        EngineParaAct(self.top, fuel_name, data, config)
        self.top.change_frame(self.OUTPUT_FRAME_NUMBER)

    @staticmethod
    def check_surveys(surveys):
        if not surveys:
            return Msg.needs_min_one_survey

    #Disabling 
    def set_buttons(self):
        self.frame.navi_buttons[0].configure(
            command=lambda: self.frame.show_message("Opcja niedostępna w obecnej wersji."))
        self.frame.navi_buttons[1].configure(
            command=lambda: self.clean())
