from typing import Optional, Type, NamedTuple, Tuple
import math
from .template import InterfaceTemplate, Data, Config
from ..head.objects import Survey, Fuel


class ImpulseOutput(NamedTuple):
    total_impulse: float 
    unit_impulse: float
    smp_time: float #ms
    jet_d: float # mm
    jet_field: float # mm
    fuel_mass: float # g
    chamber_length: float
    chamber_d: float
    a: Optional[float] = None # []


class Impulse(InterfaceTemplate):
    END_TIME_INDEX = 2

    def calculate_impulse(self, survey: Survey)\
        -> Type[ImpulseOutput]:
        fuel_mass = self.to_kg(survey.fuel_mass)
        smp_time = self.to_s(survey.sampling_time)
        jet_d = self.to_m(survey.jet_diameter)
        
        times = (survey.t0, survey.tc, survey.tk)
        values = tuple(self.cut_values(val, survey.sampling_time, times)
                       for val in survey.values)
        press_values = self.to_J(values[0])

        jet_field = math.pi * (jet_d**2) / 4
        total_impulse = self.integrate(
            press_values, smp_time)
        unit_impulse = total_impulse / fuel_mass

        if survey.type == "pressthru":
            thrust_values = values[1]
            a = self.calculate_a(
                press_values, thrust_values, jet_field)
        else:
            a = None
        return ImpulseOutput(total_impulse, unit_impulse,
            survey.sampling_time, survey.jet_diameter, jet_field,
            fuel_mass, survey.chamber_length, survey.chamber_diameter,
            a)

    @staticmethod
    def calculate_a(
        press_values: Tuple[float, ...],
        thrust_values: Tuple[float, ...],
        jet_field: float)\
        -> float:
        sum_a = float(0)
        for press, thrust in zip(press_values, thrust_values):
            if press:
                a = thrust / (press * jet_field)
            else:
                a = 0
            sum_a += a
        return sum_a / len(press_values)

    def get_results(self) -> Tuple[ImpulseOutput, ...]:
        if self.data.surveys:
            return tuple(self.calculate_impulse(survey)
                        for survey in self.data.surveys)
