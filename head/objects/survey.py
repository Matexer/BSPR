class Survey:
    def __init__(self):
        self.fuel_name = ""
        self.survey_type = ""
        self.survey_data_path = ""
        self.sampling_time = ''

        self.jet_diameter = ''
        self.chamber_length = ''
        self.chamber_diameter = ''
        self.expense_lose_factor = 0.95
        self.heat_lose_factor = 1

        self.fuel_outer_diameter = ''
        self.fuel_inner_diameter = ''
        self.fuel_length = ''
        self.fuel_mass = ''

        self.survey_comment = ""
        self.save_time = ''
        self.save_date = ''

        self.raw_values = []

    def export(self):
        return self.__dict__

    def update(self, data):
        for feature, value in data.items():
            self.__setattr__(feature, value)
