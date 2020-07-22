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
