from typing import NamedTuple, Tuple, Optional, Any
from head.objects import Survey, Fuel
from .tools import Integrals
from globals import INTEGRATION_METHODS as int_m
from globals import CALCULATION_METHODS as cal_m


class Data(NamedTuple):
    surveys: Tuple[Survey]
    times: Optional[Tuple[float]] = None
    variables: Optional[NamedTuple] = None


class Config(NamedTuple):
    integration_method: Optional[Tuple[str]]
    calculation_method: Optional[Tuple[str]] = "average"


class InterfaceTemplate:
    END_TIME_INDEX = 1  #0=t0, 1=tc, 2=tk

    def __init__(self, data: Data, config):
        self.data = data
        self.config = config
        self.__integrals = {int_m[0]: Integrals.rect_integral,
                          int_m[1]: Integrals.trapeze_integral,
                          int_m[2]: Integrals.simpson_integral}
        self.to_kg = self.to_m
        self.to_g = self.to_mm
        self.to_s = self.to_m
        self.to_ms = self.to_mm

    def integrate(self, 
        values: Tuple[float, ...], smp_time: float)\
        -> float:
        return self.__integrals[self.config.integration_method]\
               (values, smp_time)

    def cut_values(
        self,
        values: Tuple[float, ...],
        smp_time: float,
        times: Tuple[float, float, float])\
        -> Tuple[float, ...]:
        start = int(round((times[0] / smp_time), 0))
        end = int(round((times[self.END_TIME_INDEX] / smp_time), 0))

        val_length = len(values)
        max_val = max(start, end+1)

        if max_val > val_length:
            tail = [float(0) for i in range((max_val - val_length))]
            values = tuple(list(values) + tail)
        return values[start:end+1]

    @staticmethod
    def to_mm(val: float) -> float:
        return val*1000
    
    @staticmethod
    def to_mm2(val: float) -> float:
        return val*1000000

    @staticmethod
    def to_m(val: float) -> float:
        return val/1000
    
    @staticmethod
    def to_m2(val: float) -> float:
        return val/1000000

    @staticmethod
    def to_J(values: Tuple[float, ...])\
        -> Tuple[float, ...]:
        return tuple(val * 1000_000 for val in values)
