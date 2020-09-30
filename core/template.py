from typing import NamedTuple, Tuple
from head.objects import Survey, Fuel
from .tools import Integrals


class Data(NamedTuple):
    fuel: Fuel
    variables: NamedTuple
    surveys: Tuple[Survey]


class Config(NamedTuple):
    integration_method: str
    calculation_method: str


class InterfaceTemplate:
    def __init__(self, data: Data, config):
        self.integrals = Integrals
        self.data = data
        self.config = config
