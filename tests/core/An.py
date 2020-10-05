import unittest
from app.core import Data, Config, An, AnOutplut
from app.head.database import Database as db
from app.globals import INTEGRATION_METHODS as int_m
from app.globals import CALCULATION_METHODS as cal_m


class AnTest():
    def __init__(self):
        fuel_name = "Bazalt 2a"
        pressthru_surveys = db.load_surveys(fuel_name, "pressthru")
        data = Data(surveys=pressthru_surveys)
        config = Config(integration_method = "rect")

        A_and_n = An(data, config)
        results = A_and_n.get_results()
        
        for i, result in enumerate(results):
            print(f"""------------------- {i}
A = {result.total_impulse}
n = {result.unit_impulse}""")
