from ..configure import *
from .button import Button


class TopMenuButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(background=TMB_BG,
                       width=TMB_WIDTH)
