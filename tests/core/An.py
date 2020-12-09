import unittest
import tabulate as t
from typing import Tuple, NamedTuple
from app.core import Data, Config, An, AnOutput
from app.head.database import Database as db
from app.globals import INTEGRATION_METHODS, CALCULATION_METHODS, SURVEY_TYPES


class Dataset(NamedTuple):
    fuel_name: str
    data: Data
    configs: Tuple[Config, ...]
    configs_labels: Tuple[str, ...]


class OutputData(NamedTuple):
    fuel_name: str
    configs_labels: Tuple[str, ...]
    outputs: tuple


class AnTest():
    S_TYPES = "pressthru", "press"
    FUELS = "Bazalt 2a",

    def __init__(self):
        output_data = self.get_output_data()
        for output in output_data:
            self.show(output)
            ...

    def get_output_data(self):
        output_data = []
        for dataset in self.get_datasets():
            outputs = self.get_outputs(dataset)
            output_data.append(OutputData(dataset.fuel_name,
                dataset.configs_labels, outputs))
        return output_data

    def show(self, output_data: OutputData):
        print("---------------------------------")
        print(f"Paliwo {output_data.fuel_name}")
        for config, output in zip(output_data.configs_labels, output_data.outputs):
            print(config)
            print(f"A = {output.A:.3g} \t n = {output.n:.3f}\n\n")
            print(self.get_table(output.surveys_details))
            print("\n\n")
        
    def get_outputs(self, dataset):
        return [An(dataset.data, config).get_results() 
                for config in dataset.configs]

    def get_datasets(self):
        raw_configs = self.get_configs()
        return [Dataset(fuel, *self.prepare_data(fuel, raw_configs))
                for fuel in self.FUELS]
    
    def prepare_data(self, fuel, raw_configs):
        data = self.get_data(fuel)

        configs = []
        for raw_config in raw_configs[1]:
            configs.append(Config(*raw_config))
        return data, configs, raw_configs[0]

    def get_data(self, fuel_name: str):
        surveys = []
        times = []
        for s_type in self.S_TYPES:
            data = db.load_surveys(fuel_name, s_type)
            if data:
                surveys += data

        for survey in surveys:
            data = survey.values[0]
            times.append(data.index(max(data)) * survey.sampling_time)
        
        return Data(surveys, times)

    @staticmethod
    def get_configs():
        configs = ([],[])
        for i_name, i_m in INTEGRATION_METHODS.items():
            for c_name, c_m in CALCULATION_METHODS.items():
                configs[0].append(
                    str(f"M. całkowania: {i_name} \t M. obliczania: {c_name}"))
                configs[1].append((i_m, c_m))
        return configs

    @staticmethod
    def get_table(details):
        data = []
        for i, s in enumerate(details, start=1):
            headers = ("Lp.", "p\n[MPa]", "u\n[mm/s]", "t0\n[ms]", "tk\n[ms]",
                "tc\n[ms]", "Ipk\n[MPa*s]", "Śr. kryt.\ndyszy[mm]", "t\n[ms]")
            data.append((i, s.p/1000_000, s.u*1000, *s.times,
                s.Ipk/1000_000, s.jet_d ,s.point_time))
        return t.tabulate(data, headers, tablefmt='orgtbl')
