from typing import Generator
from head.messages import Messages as Msg


class DataValidator:
    """Checks an condition and returns None or error message."""

    @staticmethod
    def is_not_equal(val1, val2, name1="Wartość", name2="inna"):
        if val1 == val2:
            return Msg.cannot_be_equal(name1, name2)

    @staticmethod
    def is_equal_or_bigger_than(val1, val2, name1="Wartość", name2="inna"):
        if val1 < val2:
            return Msg.cannot_be_less_than(name1, name2)

    def is_bigger_than(
            self, val1, val2, name1="Wartość", name2="inna"):
        args = val1, val2, name1, name2

        msg = self.is_not_equal(*args)
        if msg:
            return msg
        return self.is_equal_or_bigger_than(*args)

    def is_not_equal_0(self, val, name="Wartość"):
        return self.is_not_equal(val, 0, name, "0")

    def is_bigger_than_0(self, val, name="Wartość"):
        return self.is_bigger_than(val, 0, name, "0")

    def is_equal_or_bigger_than_0(self, val, name="Wartość"):
        return self.is_equal_or_bigger_than(val, 0, name, "0")

    def are_bigger_than_0(self, values, names=None):
        if values == None:
            return None

        def make_reports():
            reports = []
            if names:
                for value, name in values, names:
                    val_name = f"Wartość \"{name}\""
                    report = self.is_bigger_than_0(value, val_name)
                    reports.append(report)
            else:
                for value in values:
                    report = self.is_bigger_than_0(value)
                    reports.append(report)
            return reports

        if isinstance(values, (list, tuple, Generator)):
            reports = make_reports()
            reports = self.__sum_up_reports(reports)
            return reports

    @staticmethod
    def __sum_up_reports(error_reports):
        if any(error_reports):
            return error_reports
        else:
            return False
