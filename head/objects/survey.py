from .template import Template


class Survey(Template):
    ARGS_NUM = 12

    def __init__(self):
        self.type: str = ""
        self.sampling_time: float = 0

        self.jet_diameter: float = 0
        self.chamber_length: float = 0
        self.chamber_diameter: float = 0
        self.expense_lose_factor: float = 0
        self.heat_lose_factor: float = 0

        self.fuel_outer_diameter: float = 0
        self.fuel_inner_diameter: float = 0
        self.fuel_length: float = 0
        self.fuel_mass: float = 0

        self.comment: str = ""

        self.raw_values = []
        self.values = []
        self.multipliers = []
        self.t0: float = 0
        self.tk: float = 0
        self.tc: float = 0

        super().__init__()
