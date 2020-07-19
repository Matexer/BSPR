from ..configure import *
from .button import Button


class LeftMenuButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(background=LMB_BG,
                       wrap=LMB_wrap,
                       width=LMB_width,
                       foreground=LMF_TEXT_COLOR)
