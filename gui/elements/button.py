import tkinter as tk


class Button(tk.Button):
    def __init__(self, top):
        tk.Button.__init__(self, top)
        self.configure(borderwidth=0,
                       highlightthickness=0)
