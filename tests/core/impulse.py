import unittest
from app.core import Data, Config, Impulse, ImpulseOutput
from app.head.database import Database as db


class ImpulseTest():
    def __init__(self):
        fuel_name = "Bazalt 2a"
        pressthru_surveys = db.load_surveys(fuel_name, "pressthru")
        data = Data(surveys=pressthru_surveys)
        config = Config(0)

        impulse = Impulse(data, config)
        results = impulse.get_results()
        
        for i, result in enumerate(results):
            print(f"""------------------- {i}
Ic = {result.total_impulse} N⋅s
I1 = {result.unit_impulse} N⋅s/kg""")
