import math
from typing import Tuple, NamedTuple
from scratch.statistic import correlation, standard_deviation, mean
from .template import InterfaceTemplate, Data, Config
from ..head.objects import Survey


class AnOutplut(NamedTuple):
    A: float
    n: float


class An(InterfaceTemplate):
    END_TIME_INDEX = 2

    def get_p_u(self, surveys: Tuple[Survey, ...])\
        -> Tuple[Tuple[float, float], ...]:
        values = list()
        if self.config.calculation_method == "average":
            for survey in surveys:
                values.append(self.get_average_p_u(survey))
        else:
            for survey, t in zip(surveys, self.data.times):
                values.append(self.get_pointed_p_u(survey, t))
        return tuple(values)

    def get_average_p_u(self, survey: Survey)\
        -> Tuple[float, float]:
        smp_time = self.to_s(survey.sampling_time)
        times = (survey.t0, survey.tc, survey.tk)

        values = tuple(self.cut_values(val, smp_time, times)
                       for val in survey.values)
        press_values = self.to_J(values[0])

        Ipk = self.integrate(press_values, smp_time)
        ave_p = Ipk / survey.tk

        e = (survey.fuel_outer_diameter - survey.fuel_inner_diameter) / 4
        ave_u = e / survey.tk
        return ave_p, ave_u

    def get_pointed_p_u(self, survey: Survey, time: float)\
        -> Tuple[float, float]:
        smp_time = self.to_s(survey.sampling_time)
        times = (survey.t0, survey.tc, survey.tk)

        press_values = self.to_J(survey.values[0])
        index = int(round(time / smp_time, 0))
        p = press_values[index]

        press_values = tuple(self.cut_values(val, smp_time, times)
                             for val in press_values)  
        Ip = self.integrate(press_values, smp_time)
        D = survey.fuel_outer_diameter
        d = survey.fuel_inner_diameter
        L = survey.fuel_length
        V = math.pi*((D/2)**2 - (d/2)**2)*L
        S = (2*math.pi*d/2*L) + (2*math.pi*D/2*L) +\
             2*(math.pi*((D/2)**2 - (d/2)**2))
        u = (V * p) / (S * Ip)
        return p, u

    def calculate_An(self, surveys: Tuple[Survey, ...])\
        -> Tuple[float, float]:
        cords = self.get_p_u(surveys)
        x = tuple(math.log10(p) for p, _ in cords)
        y = tuple(math.log10(u) for _, u in cords)
        n = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
        A = math.exp(mean(y) - n * mean(x))
        return A, n

    def get_results(self):
        return AnOutplut(self.calculate_An(self.data.surveys))
