import datetime


class Template:
    ARGS_NUM = 1

    def __init__(self):
        time = datetime.datetime.today()
        self.save_time = time.strftime('%H:%M:%S')
        self.save_date = time.strftime('%d.%m.%Y')

        self.edit_time = self.save_time
        self.edit_date = self.save_date

    def export(self):
        return self.__dict__

    def update(self, data):
        if isinstance(data, dict):
            for feature, value in data.items():
                self.__setattr__(feature, value)
        elif isinstance(data, (list, tuple)):
            for feature, value in zip(list(self.__dict__.keys())[:self.ARGS_NUM], data):
                self.__setattr__(feature, value)
        self.update_timedata()

    def update_timedata(self):
        time = datetime.datetime.today()
        self.edit_time = time.strftime('%H:%M:%S')
        self.edit_date = time.strftime('%d.%m.%Y')
