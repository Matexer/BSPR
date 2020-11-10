from typing import NamedTuple, Tuple, Optional, Any, Union
from ..head.objects import Survey, Fuel
from .tools import Integrals


class Data(NamedTuple):
    surveys: Tuple[Survey, ...]
    times: Optional[Tuple[float, ...]] = None
    variables: Optional[NamedTuple] = None


class Config(NamedTuple):
    integration_method: Optional[int]
    #0-rect, 1-trapeze, 2-simpson
    calculation_method: Optional[int] = 0
    #0-mean, 1-moment


class DesignationTemplate:
    def __init__(self, data: Data, config: Config):
        self.data = data
        self.config = config
        self.__integrals = (Integrals.rect,
                            Integrals.trapeze,
                            Integrals.simpson)

        self.g_to_kg = lambda v: self.multiply(0.001, v)
        self.kg_to_g = lambda v: self.multiply(1000, v)
        self.mm_to_m = lambda v: self.multiply(0.001, v)
        self.m_to_mm = lambda v: self.multiply(1000, v)
        self.N_to_kN = lambda v: self.multiply(0.001, v)
        self.kN_to_N = lambda v: self.multiply(1000, v)
        self.ms_to_s = lambda v: self.multiply(0.001, v)
        self.s_to_ms = lambda v: self.multiply(1000, v)

        self.MPa_to_Pa = lambda v: self.multiply(1000_000, v)
        self.hPa_to_Pa = lambda v: self.multiply(100, v)
        self.Pa_to_MPa = lambda v: self.multiply(0.000_001, v)
        self.MJ_to_J = lambda v: self.multiply(1000_000, v)
        self.m2_to_mm2 = lambda v: self.multiply(1000_000, v)
        self.mm2_to_m2 = lambda v: self.multiply(0.000_001, v)

    def integrate(self, 
        values: Tuple[float, ...], smp_time: float)\
        -> float:
        return self.__integrals[self.config.integration_method]\
               (values, smp_time)

    @staticmethod
    def cut_values(values: Tuple[float, ...], smp_time: float,
        times: Tuple[float, float, float], end_t_index: int)\
        -> Tuple[float, ...]:
        start = int(round((times[0] / smp_time), 0))
        end = int(round((times[end_t_index] / smp_time), 0))
        if end >= len(values):
            return values[start:]
        return values[start:end+1]

    @staticmethod
    def multiply(m: Union[int, float],
        vals: Union[Tuple[float, ...], float])\
        -> Union[Tuple[float, ...], float]:
        if isinstance(vals, float):
            return vals * m
        return tuple(val * m for val in vals)
