class Fuel:
    def __init__(self):
        self.name = ""
        self.outer_diameter = ""
        self.inner_diameter = ""
        self.length = ""
        self.mass = ""
        self.strength = ""
        self.k = 1.25
        self.comment = ""

        self.save_time = 0
        self.save_date = 0

    def export(self):
        return self.__dict__

    def update(self, data):
        if isinstance(data, dict):
            for feature, value in data.items():
                self.__setattr__(feature, value)
        elif isinstance(data, (list, tuple)):
            for feature, value in zip(list(self.__dict__.keys())[:7], data):
                self.__setattr__(feature, value)

    def save_timedata(self):
        pass