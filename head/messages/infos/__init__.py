from .comparisons import ComparisonMessages


class LiveMessages:
    @staticmethod
    def needs_to_choose(name):
        return "Należy wybrać {}.".format(name)

    @staticmethod
    def needs_to_fulfil_field(name):
        return "Należy uzupełnić pole \"{}\"".format(name)


class InfoMessages(ComparisonMessages, LiveMessages):
    saved_successfully = "Zapisano pomyślnie."
    must_be_number = "Wartość musi być liczbą."
    needs_to_choose_fuel = LiveMessages.needs_to_choose("paliwo")
    needs_2_diff_jets_diam = LiveMessages.needs_to_choose(
        "co najmniej dwa pomiary o różnych średnicach krytycznych dyszy")
