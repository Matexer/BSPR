import math
from typing import Tuple, NamedTuple, Optional, List
from statistics import stdev, variance, mean
from .template import InterfaceTemplate, Data, Config
from ..head.objects import Survey


class SurveyDetails(NamedTuple):
    p: float
    u: float
    times: Tuple[float, float, float]
    Ipk: float
    point_time: Optional[float]


class AnOutplut(NamedTuple):
    A: float
    n: float
    surveys_details: Tuple[SurveyDetails, ...]


class An(InterfaceTemplate):
    END_TIME_INDEX = 2


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.details: List[SurveyDetails, ...] = []

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

        values = tuple(self.cut_values(val, survey.sampling_time, times)
                       for val in survey.values)
        press_values = self.to_J(values[0])

        Ipk = self.integrate(press_values, smp_time)
        ave_p = Ipk / survey.tk

        e = (survey.fuel_outer_diameter - survey.fuel_inner_diameter) / 4
        ave_u = e / survey.tk

        self.details.append(SurveyDetails(ave_p, ave_u, times, Ipk, None))
        return ave_p, ave_u

    def get_pointed_p_u(self, survey: Survey, time: float)\
        -> Tuple[float, float]:
        smp_time = self.to_s(survey.sampling_time)
        times = (survey.t0, survey.tc, survey.tk)

        press_values = self.to_J(survey.values[0])
        index = int(round(time / survey.sampling_time, 0))
        p = press_values[index]

        press_values = tuple(self.cut_values(val, survey.sampling_time, times)
                             for val in press_values)  
        Ip = self.integrate(press_values, smp_time)
        D = survey.fuel_outer_diameter
        d = survey.fuel_inner_diameter
        L = survey.fuel_length
        V = math.pi*((D/2)**2 - (d/2)**2)*L
        S = (2*math.pi*d/2*L) + (2*math.pi*D/2*L) +\
             2*(math.pi*((D/2)**2 - (d/2)**2))
        u = (V * p) / (S * Ip)

        self.details.append(SurveyDetails(p, u, times, Ip, time))
        return p, u

    def calculate_An(self, surveys: Tuple[Survey, ...])\
        -> Tuple[float, float]:
        cords = self.get_p_u(surveys)
        xs = tuple(math.log(p) for p, _ in cords)
        ys = tuple(math.log(u) for _, u in cords)
        n = self.correlation(xs, ys) * stdev(ys) / stdev(xs)
        A = math.exp(mean(ys) - n * mean(xs))
        return A, n

    def correlation(self, xs: Tuple[float, ...], ys: Tuple[float, ...])\
        -> float:
        stdev_x = stdev(xs)
        stdev_y = stdev(ys)
        if stdev_x > 0 and stdev_y > 0:
            return self.covariance(xs, ys) / stdev_x / stdev_y
        else:
            return 0

    def covariance(self, xs: Tuple[float, ...], ys: Tuple[float, ...])\
        -> float:
        return self.dot(self.de_mean(xs), self.de_mean(ys)) / (len(xs) - 1)

    @staticmethod
    def dot(xs: Tuple[float, ...], ys: Tuple[float, ...])\
        -> float:
        return sum(x_i * y_i for x_i, y_i in zip(xs, ys))

    @staticmethod
    def de_mean(xs: Tuple[float, ...])\
        -> Tuple[float, ...]:
        x_bar = mean(xs)
        return tuple(x - x_bar for x in xs)
    
    def get_results(self) -> AnOutplut:
        return AnOutplut(*self.calculate_An(self.data.surveys), self.details)
