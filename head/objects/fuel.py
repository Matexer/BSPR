class Fuel:
    def __init__(self):
        self.name = ""
        self.mass = ""
        self.comment = ""
        self.outer_diameter = ""
        self.inner_diameter = ""
        self.length = ""
        self.strength = ""
        self.k = 1.25
        self.save_time = 0

    def export(self):
        return self.__dict__

    def update(self, data):
        for feature, value in data.items():
            self.__setattr__(feature, value)
