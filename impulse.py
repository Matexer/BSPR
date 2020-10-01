import unittest
from core import Data, Config, Impulse, ImpulseOutput
from head import database as db
from globals import INTEGRATION_METHODS as int_m
from globals import CALCULATION_METHODS as cal_m


class ImpulseTest():
    def __init__(self):
        fuel_name = "ttrr"
        pressthru_surveys = db.load_surveys(fuel_name, "pressthru")
        data = Data(surveys=pressthru_surveys)
        config = Config(integration_method = "rect")

        impulse = Impulse(data, config)
        results = impulse.get_results()
        
        for result in results:
            print(result.total_impulse)

ImpulseTest()
