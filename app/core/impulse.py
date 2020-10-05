from typing import Optional, Type, Generator, Tuple
import math
from .template import InterfaceTemplate, Data, Config
from ..head.objects import Survey, Fuel


class ImpulseOutput():
    total_impulse: float 
    unit_impulse: float
    smp_time: float #ms
    jet_d: float # mm
    jet_field: float # mm
    fuel_mass: float # g
    a: Optional[float] = None # []


class Impulse(InterfaceTemplate):
    END_TIME_INDEX = 2

    def calculate_impulse(self, survey: Survey)\
        -> ImpulseOutput:
        o = ImpulseOutput()
        o.fuel_mass = self.to_kg(survey.fuel_mass)
        o.smp_time = self.to_s(survey.sampling_time)
        o.jet_d = self.to_m(survey.jet_diameter)
        
        times = (survey.t0, survey.tc, survey.tk)
        values = tuple(self.cut_values(val, o.smp_time, times)
                       for val in survey.values)
        press_values = self.to_J(values[0])

        o.jet_field = math.pi * (o.jet_d**2) / 4
        o.total_impulse = self.integrate(
            press_values, o.smp_time)
        o.unit_impulse = o.total_impulse / o.fuel_mass

        if survey.type == "pressthru":
            thrust_values = values[1]
            o.a = self.calculate_a(
                press_values, thrust_values, o.jet_field)
        return o

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
