import tkinter as tk
from gui.configure import *
from gui.elements import TopMenuButton


class TopMenuFrame(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)
        self.configure(background=TMF_BG)
        self.fuel_list_btn = TopMenuButton(self)
        self.fuel_list_btn.grid()
        self.fuel_list_btn.configure(text='''Lista paliw''')

        self.survey_list_btn = TopMenuButton(self)
        self.survey_list_btn.grid(row=0, column=1)
        self.survey_list_btn.configure(text='''Lista pomiarów''')
