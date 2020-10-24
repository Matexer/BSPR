from typing import List
from .template import InterfaceTemplate, Data, Config


class EnginePara(InterfaceTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.details: float

    def K0_k(self):
        ...
    
    def K_k(self):
        ...
    
    def Fw(self):
        ...

    def Xa(self):
        ...

    def fi_2(self):
       ... 

    #     if survey.type == "pressthru":
    #         thrust_values = values[1]
    #         a = self.calculate_a(
    #             press_values, thrust_values, jet_field)
    #     else:
    #         a = None
    #     return ImpulseOutput(total_impulse, unit_impulse,
    #         survey.sampling_time, survey.jet_diameter, jet_field,
    #         fuel_mass, survey.chamber_length, survey.chamber_diameter)

    # @staticmethod
    # def calculate_a(
    #     press_values: Tuple[float, ...],
    #     thrust_values: Tuple[float, ...],
    #     jet_field: float)\
    #     -> float:
    #     sum_a = float(0)
    #     for press, thrust in zip(press_values, thrust_values):
    #         if press:
    #             a = thrust / (press * jet_field)
    #         else:
    #             a = 0
    #         sum_a += a
    #     return sum_a / len(press_values)