from .converter import DataConverter
from .validator import DataValidator


class DataManager(DataValidator, DataConverter):
    ...
