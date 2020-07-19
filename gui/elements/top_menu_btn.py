from ..configure import *
from .button import Button


class TopMenuButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(background="green",
                       width=TMB_width)
