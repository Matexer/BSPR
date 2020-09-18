from typing import List, Tuple, AnyStr, Sequence, Any
from .messages import Messages


class DataConverter(Messages):
    """Container of methods which gets a variables and type to be converted.
    Returns list of converted values and report of conversion.

     Example: to_float([2, 3, "egg"]) -> [2, 3, None], [0, 0, "Error msg"]"""
    def to_float(self, data) -> Any[Tuple[float or AnyStr], float or AnyStr]:
        if isinstance(data, Sequence):
            converted_data = []
            for value in data:
                try:
                    converted_data.append(float(value))
                except ValueError:
                    converted_data.append(self.must_be_number)
            return converted_data
        else:
            try:
                return float(data)
            except ValueError:
                return self.must_be_number