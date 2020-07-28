from gui import GUI


class Application:
    def __init__(self):
        self.top = self.start()
        self.frames = self.top.frames

    @staticmethod
    def start():
        gui = GUI()
        top = gui.start()
        return top

    def fill_lists(self):
        fuels_list_frame = self.frames[0]
        survey_list_frames = self.frames[2]
