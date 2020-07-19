from ..configure import *
from .button import Button


class LeftMenuButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(background="green",
                       wrap=LMB_wrap,
                       width=LMB_width)
