class ComparisonMessages:
    must_be_bigger_than_0 = "Wartość musi być większa niż 0."
    must_be_bigger_or_equal_0 = "Wartość musi być większa lub równa 0."

    @classmethod
    def cannot_be_less_than(cls, val1="Wartość", val2="inna"):
        return "{0} nie może być mniejsza niż {1}.".format(val1, val2)

    @classmethod
    def cannot_be_bigger_than(cls, val1="Wartość", val2="inna"):
        return "{0} nie może być większa niż {1}.".format(val1, val2)

    @classmethod
    def cannot_be_equal(cls, val1="Wartość", val2="innej"):
        return "{0} nie może być równa {1}.".format(val1, val2)
