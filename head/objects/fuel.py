from .template import Template


class Fuel(Template):
    ARGS_NUM = 8

    def __init__(self):
        self.name = None

        self.outer_diameter = None
        self.inner_diameter = None
        self.length = None
        self.mass = None

        self.strength = None
        self.k = 1.25

        self.comment = None

        super().__init__()
