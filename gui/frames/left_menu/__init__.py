import tkinter as tk
from gui.configure import *
from gui.elements import LeftMenuButton


class LeftMenuFrame(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)
        self.configure(background=LMF_BG)
        self.designate_label = tk.Label(self)
        self.designate_label.pack(side="top")
        self.designate_label.configure(text='''Wyznacz''')

        self.designate_imp_btn = LeftMenuButton(self)
        self.designate_imp_btn.pack(side="top")
        self.designate_imp_btn.configure(text='''Impuls jednostkowy''')

        self.designate_An_btn = LeftMenuButton(self)
        self.designate_An_btn.pack(side="top")
        self.designate_An_btn.configure(text='''Współczynniki A i n prawa szybkości spalania''')

        self.designate_engine_para_btn = LeftMenuButton(self)
        self.designate_engine_para_btn.pack(side="top")
        self.designate_engine_para_btn.configure(text='''Współczynniki strat gazo-
dynamicznych i cieplnych''')
