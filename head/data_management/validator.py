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

    @classmethod
    def is_bigger_than(
            cls, val1, val2, name1="Wartość", name2="inna"):
        args = val1, val2, name1, name2

        msg = cls.is_not_equal(*args)
        if msg:
            return msg
        return cls.is_equal_or_bigger_than(*args)

    @classmethod
    def is_not_equal_0(cls, val, name="Wartość"):
        return cls.is_not_equal(val, 0, name, "0")

    @classmethod
    def is_bigger_than_0(cls, val, name="Wartość"):
        return cls.is_bigger_than(val, 0, name, "0")

    @classmethod
    def is_equal_or_bigger_than_0(cls, val, name="Wartość"):
        return cls.is_equal_or_bigger_than(val, 0, name, "0")

    @classmethod
    def are_bigger_than_0(cls, values, names=None):
        if isinstance(values, (list, tuple, Generator)):
            reports = []
            if names:
                for value, name in zip(values, names):
                    val_name = f"Wartość \"{name}\""
                    report = cls.is_bigger_than_0(value, val_name)
                    if not report:
                        report = 0
                    reports.append(report)
            else:
                for value in values:
                    report = cls.is_bigger_than_0(value)
                    if not report:
                        report = 0
                    reports.append(report)
            reports = cls.__sum_up_reports(reports)
            return reports

    @staticmethod
    def __sum_up_reports(error_reports):
        if any(error_reports):
            return error_reports
        else:
            return False
