import tkinter as tk
from .TopWindow import TopWindow
from globals import *


class GUI:
    def __init__(self):
        self.top = None

    def start(self):
        root = tk.Tk()
        top = TopWindow(root)
        root.title(TITLE)
        root.geometry("1000x600")
        root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
        root.mainloop()
        self.top = top
        return top
