from .template import Template


class Survey(Template):
    ARGS_NUM = 12

    def __init__(self):
        self.survey_type = None
        self.sampling_time = None

        self.jet_diameter = None
        self.chamber_length = None
        self.chamber_diameter = None
        self.expense_lose_factor = None
        self.heat_lose_factor = None

        self.fuel_outer_diameter = None
        self.fuel_inner_diameter = None
        self.fuel_length = None
        self.fuel_mass = None

        self.survey_comment = None

        self.raw_values = None
        self.multiplier = None
        self.t0 = None
        self.tk = None
        self.tc = None

        super().__init__()
