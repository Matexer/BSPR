from ....core import Impulse, ImpulseOutput, Data, Config
from ....gui.TopWindow import TopWindow


class CalculationActTemplate:
    FRAME_NUMBER = 12


    def __init__(self, top: TopWindow, 
        f_name: str, data: Data, config: Config):
        self.frame = top.frames[self.FRAME_NUMBER]
        self.clean_frame()

    def clean_frame(self):
        for child in self.frame.interior.winfo_children():
            child.destroy()