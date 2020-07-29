import tkinter as tk
from gui.configure import *


class TitleLabel(tk.Label):
    def __init__(self, top):
        tk.Label.__init__(self, top)
        self.configure(background=TL_BG,
                       foreground=TL_FG,
                       font="bold",
                       pady=7,
                       anchor="w")


class SubtitleLabel(tk.Label):
    def __init__(self, top):
        tk.Label.__init__(self, top)
        self.configure(background=STL_BG,
                       foreground=STL_FG,
                       pady=5,
                       anchor="w")


class MessageLabel(tk.Label):
    def __init__(self, top, text=''):
        tk.Label.__init__(self, top)
        self.configure(text=text,
                       font="bold",
                       foreground="green",
                       pady=5,
                       anchor="w")

    def set_text(self, text):
        self.configure(text=text)

    def set_color(self, color):
        self.configure(foreground=color)
