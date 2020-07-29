from gui import GUI
from .acts import *


class Application:
    def __init__(self):
        self.gui, self.top = self.start()
        self.frames = self.top.frames
        self.acts = self.load_acts()
        self.gui.run_loop()

    @staticmethod
    def start():
        gui = GUI()
        top = gui.start()
        return gui, top

    def load_acts(self):
        acts = [AddFuelAct(self.top)]
        return acts
