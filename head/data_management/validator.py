from head.messages import Messages as Msg


class DataValidator:
    """Checks an condition and returns None or error message."""

    @staticmethod
    def is_not_equal(val1, val2, name1="Wartość", name2="inna"):
        if val1 == val2:
            return Msg.cannot_be_equal(name1, name2)

    @staticmethod
    def is_bigger_or_equal_than(val1, val2, name1="Wartość", name2="inna"):
        if val1 < val2:
            return Msg.cannot_be_less_than(name1, name2)

    def is_bigger_than(
            self, val1, val2, name1="Wartość", name2="inna"):
        args = val1, val2, name1, name2

        msg = self.is_not_equal(*args)
        if msg:
            return msg

        return self.is_bigger_or_equal_than(*args)
