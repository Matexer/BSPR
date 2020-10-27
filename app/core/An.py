import math
from typing import Tuple, NamedTuple, Optional, List
from statistics import stdev, variance, mean
from .template import InterfaceTemplate, Data, Config
from ..head.objects import Survey


class SurveyDetails(NamedTuple):
    p: float #Pa
    u: float #m/s
    times: Tuple[float, float, float] #ms
    Ipk: float
    jet_d: float #mm
    d_min: float #mm2
    point_time: Optional[float] #ms


class AnOutplut(NamedTuple):
    A: float
    n: float
    surveys_details: Tuple[SurveyDetails, ...]


class An(InterfaceTemplate):
    END_TIME_INDEX = 1


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.details: List[SurveyDetails, ...] = []

    def get_p_u(self, surveys: Tuple[Survey, ...])\
        -> Tuple[Tuple[float, float], ...]:
        values = list()
        if self.config.calculation_method == 0: #average
            for survey in surveys:
                values.append(self.get_average_p_u(survey))
        else:
            for survey, t in zip(surveys, self.data.times):
                values.append(self.get_pointed_p_u(survey, t))
        return tuple(values)

    def get_average_p_u(self, survey: Survey)\
        -> Tuple[float, float]:
        smp_time = self.ms_to_s(survey.sampling_time)
        times = (survey.t0, survey.tk, survey.tc)

        values = tuple(self.cut_values(val, survey.sampling_time, times)
                       for val in survey.values)
        press_values = self.MPa_to_Pa(values[0])

        tk = self.ms_to_s(survey.tk)
        Ipk = self.integrate(press_values, smp_time)
        ave_p = Ipk / tk

        d = self.mm_to_m(survey.fuel_inner_diameter)
        D = self.mm_to_m(survey.fuel_outer_diameter)
        e = (D - d) / 4
        ave_u = e / tk

        F_min = self.F_min(survey)

        self.details.append(SurveyDetails(ave_p, ave_u,
            times, Ipk, survey.jet_diameter, F_min, None))
        return ave_p, ave_u

    def get_pointed_p_u(self, survey: Survey, time: float)\
        -> Tuple[float, float]:
        smp_time = self.ms_to_s(survey.sampling_time)
        times = (survey.t0, survey.tk, survey.tc)

        press_values = self.MPa_to_Pa(survey.values[0])
        index = int(round(time / survey.sampling_time, 0))
        p = press_values[index]

        press_values = self.cut_values(
            press_values, survey.sampling_time, times)
        Ip = self.integrate(press_values, smp_time)
        D = self.mm_to_m(survey.fuel_outer_diameter)
        d = self.mm_to_m(survey.fuel_inner_diameter)
        L = self.mm_to_m(survey.fuel_length)
        V = math.pi*((D/2)**2 - (d/2)**2)*L
        S = (2*math.pi*d/2*L) + (2*math.pi*D/2*L) +\
             2*(math.pi*((D/2)**2 - (d/2)**2))
        u = (V * p) / (S * Ip)

        F_min = self.F_min(survey)

        self.details.append(SurveyDetails(p, u, times, Ip,
            survey.jet_diameter, F_min, time))
        return p, u

    def calculate_An(self, surveys: Tuple[Survey, ...])\
        -> Tuple[float, float]:
        cords = self.get_p_u(surveys)
        xs = tuple(math.log(p) for p, _ in cords)
        ys = tuple(math.log(u) for _, u in cords)
        n = self.correlation(xs, ys) * stdev(ys) / stdev(xs)
        A = math.exp(mean(ys) - n * mean(xs))
        return A, n

    def F_min(self, survey: Survey)\
        -> float:
        w = self.data.variables.w
        fi = survey.heat_lose_factor
        lam = survey.expense_lose_factor
        fp = self.MPa_to_Pa(self.data.variables.fuel.strength)
        k = self.data.variables.fuel.k

        D_ch = self.mm_to_m(survey.chamber_diameter)
        D = self.mm_to_m(survey.fuel_outer_diameter)
        d = self.mm_to_m(survey.fuel_inner_diameter)

        F_ch = math.pi * D_ch**2 / 4
        F_f = math.pi * (D - d)**2 / 4

        K0 = ((2 / (k + 1))**(1/(k-1))) * math.sqrt((2*k)/(k+1))
        Fp = F_ch - F_f
        Fmin = (w * Fp) / (fi * K0 * math.sqrt(lam * fp))

        return self.m_to_mm(2 * math.sqrt(Fmin / math.pi))

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
