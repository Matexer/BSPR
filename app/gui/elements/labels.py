import tkinter as tk
from ..configure import *


class Label(tk.Label):
    def __init__(self, top):
        super().__init__(top)

    def set_text(self, text):
        self.configure(text=text)

    def set_color(self, color):
        self.configure(foreground=color)


class TitleLabel(Label):
    def __init__(self, top):
        super().__init__(top)
        self.configure(background=TL_BG,
                       foreground=TL_FG,
                       font="bold",
                       pady=7,
                       anchor="w")


class SubtitleLabel(Label):
    def __init__(self, top):
        super().__init__(top)
        self.configure(background=STL_BG,
                       foreground=STL_FG,
                       pady=5,
                       anchor="w")


class MessageLabel(Label):
    def __init__(self, top, text=''):
        super().__init__(top)
        self.configure(text=text,
                       font="bold",
                       foreground="green",
                       pady=5,
                       anchor="w")


