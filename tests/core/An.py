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
        config = Config("rect", "average")

        A_and_n = An(data, config)
        results = A_and_n.get_results()
        details = results.surveys_details

        self.show_result(results.A , results.n)
        self.show_details(details)
 
    @staticmethod
    def show_result(A, n):
        print(f"""-------------------
A = {A}
n = {n}""")

    @staticmethod
    def show_details(details):
        for s in details:
            print(f"p = {s.p}; u = {s.u}; t0 = {s.times[0]}; tk = {s.times[1]}",
            f"tc = {s.times[2]}; Ipk = {s.Ipk}; t = {s.point_time}")
