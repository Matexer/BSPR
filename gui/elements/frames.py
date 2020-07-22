import tkinter as tk
from gui.configure import AF_BG


class ActionFrame(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)
        self.configure(background=AF_BG)
