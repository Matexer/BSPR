from .gui import GUI
from .head.acts import load_acts


class Application:
    def __init__(self):
        gui = GUI()
        load_acts(gui.start())
        gui.run_loop()
