import unittest
from ...core import Data, Config, Impulse, ImpulseOutput
from head import database as db
from globals import INTEGRATION_METHODS as int_m
from globals import CALCULATION_METHODS as cal_m


class ImpulseTest():
    def __init__(self):
        fuel_name = "Bazalt 2a"
        pressthru_surveys = db.load_surveys(fuel_name, "pressthru")
        data = Data(surveys=pressthru_surveys)
        config = Config(integration_method = "rect")

        impulse = Impulse(data, config)
        results = impulse.get_results()
        
        for i, result in enumerate(results):
            print(f"""------------------- {i}
Ic = {result.total_impulse}
I1 = {result.unit_impulse}
a = {result.a}""")

ImpulseTest()
