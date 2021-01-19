from .gui import GUI
from .head.acts import load_acts, test_db


class Application:
    def __init__(self):
        gui = GUI()
        test_db()
        load_acts(gui.start())
        gui.run_loop()
