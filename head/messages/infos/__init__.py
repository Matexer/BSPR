from .comparisons import ComparisonMessages


class InfoMessages(ComparisonMessages):
    saved_successfully = "Zapisano pomyślnie."
    must_be_number = "Wartość musi być liczbą."

    @classmethod
    def needs_to_choose(cls, name):
        return "Należy wybrać {}.".format(name)

    needs_to_choose_fuel = needs_to_choose("paliwo")
