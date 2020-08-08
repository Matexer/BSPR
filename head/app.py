from gui import GUI
from .acts import load_acts


class Application:
    def __init__(self):
        gui, top = self.start_gui()
        self.acts = load_acts(top)
        gui.run_loop()

    @staticmethod
    def start_gui():
        gui = GUI()
        top = gui.start()
        return gui, top
