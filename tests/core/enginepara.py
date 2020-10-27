import tabulate as t
from app.head.acts.config_calculation.engine_para import EngineParaVariables
from app.core import Data, Config, EnginePara, EngineParaOutput
from app.head.database import Database as db


class EngineParaTest:
    def __init__(self):
        fuel_name = "Bazalt 2a"

        pressthru_surveys = db.load_surveys(fuel_name, "pressthru")
        fuel = db.load_fuel(fuel_name)

        da = float(18) #mm
        pz = float(1013) #hPa
        I1 = float(5000) #kN*s/kg
        g = float(9.81) #m/s2
        variables = EngineParaVariables(fuel, da, pz, I1, g)

        data = Data(pressthru_surveys, variables=variables)
        config = Config(0)

        enginepara = EnginePara(data, config)
        results = enginepara.get_results()

        headers = ("fi1", "fi2", "lam", "K0_k", "z_a", "Xa", "Fw",
            "K_k", "Fmin\n[mm2]", "R\n[N*s]", "P\n[MPa*s]")
        values = []
        for val in results:
            values.append(val)

        data = values, 
        print(t.tabulate(data, headers, tablefmt='orgtbl'))
