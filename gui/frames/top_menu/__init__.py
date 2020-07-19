import tkinter as tk
from gui.configure import *
from gui.elements import TopMenuButton


class TopMenuFrame(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)
        self.configure(background=TMF_BG)

        self.fuel_list_btn = TopMenuButton(self)
        self.fuel_list_btn.pack(side="left")
        self.fuel_list_btn.configure(text='''Lista paliw''')

        self.survey_list_btn = TopMenuButton(self)
        self.survey_list_btn.pack(side="left")
        self.survey_list_btn.configure(text='''Lista pomiarów''')

        self.configure_btn = TopMenuButton(self)
        self.configure_btn.pack(side="right")
        self.configure_btn.configure(text='Konfiguracja')
