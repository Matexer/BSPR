from typing import Generator
from .messages import Messages as Msg


class DataConverter:
    """Container of methods which gets a variables and type to be converted.
    Returns list of converted values and report of conversion.

     Example1: to_float([2, 3, "egg"]) -> [2, 3, None], [0, 0, "Error msg"]
     Example2: to_float([2, 3, 4]) -> [2, 3, 4], False
     Example3: to_float(2) -> 2, False
     Example4: to_float(False) -> 0, False
     Example5: to_float("Egg") -> None, "Error msg"
     """

    def to_float(self, data):
        exceptions = (ValueError, TypeError)
        if isinstance(data, (list, tuple, Generator)):
            converted_data = []
            error_reports = []
            for value in data:
                report = 0
                try:
                    value = value if isinstance(value, float) else float(value)
                except exceptions:
                    value = None
                    report = Msg.must_be_number
                finally:
                    converted_data.append(value)
                    error_reports.append(report)
            error_reports = self.__sum_up_reports(error_reports)
            return converted_data, error_reports
        else:
            try:
                return float(data), False
            except exceptions:
                return None, Msg.must_be_number

    @staticmethod
    def __sum_up_reports(error_reports):
        if any(error_reports):
            return error_reports
        else:
            return False