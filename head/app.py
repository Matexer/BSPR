from gui import GUI
from .acts import *


class Application:
    def __init__(self):
        gui, top = self.start()
        self.acts = self.load_acts(top)
        gui.run_loop()

    @staticmethod
    def start():
        gui = GUI()
        top = gui.start()
        return gui, top

    @staticmethod
    def load_acts(top):
        acts = [AddFuelAct(top),
                FuelsListAct(top)]
        return acts
