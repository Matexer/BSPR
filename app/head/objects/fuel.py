from .template import Template


class Fuel(Template):
    ARGS_NUM = 8

    def __init__(self):
        self.name: str = ""

        self.outer_diameter: float = 0
        self.inner_diameter: float = 0
        self.length: float = 0
        self.mass: float = 0

        self.strength: float = 0
        self.k = 1.25

        self.comment: str = ""
        super().__init__()
