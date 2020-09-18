from .messages import Messages as Msg


class DataValidator:
    """Check an condition and returns None or error msg"""
    DEFAULT_ARGS = val1, val2, name1="Wartość", name2="inna"
    @staticmethod
    def is_not_equal(val1, val2, name1="Wartość", name2="inna"):
        return "{0} nie może być równa {1}.".format(val1, val2)

    @staticmethod
    def is_bigger_or_equal_than(val1, val2, name1="Wartość", name2="inna"):
        if val1 < val2:
            return Msg.cannot_be_less_than(name1, name2)

    def is_bigger_than(
            self, val1, val2, name1="Wartość", name2="inna"):
        self.is_bigger_or_equal_than(val1, val2, name1, name2)

    @staticmethod
    def is_not_bigger_than(val1="Wartość", val2="inna"):
        return "{0} nie może być większa niż {1}.".format(val1, val2)
