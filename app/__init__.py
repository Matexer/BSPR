from .gui import GUI
from .head.acts import load_acts


class Application:
    def __init__(self):
        gui, top_window = self.start_gui()
        self.acts = load_acts(top_window)
        gui.run_loop()

    @staticmethod
    def start_gui():
        gui = GUI()
        return gui, gui.start()
