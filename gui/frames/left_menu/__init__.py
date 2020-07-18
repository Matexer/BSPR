import tkinter.ttk as ttk
from ...elements import LeftMenuButton


class LeftMenuFrame(ttk.Frame):
    grid_config = {"sticky": "W"}

    def __init__(self, top):
        ttk.Frame.__init__(self, top)
        self.designate_label = ttk.Label(self)
        self.designate_label.grid(**self.grid_config)
        self.designate_label.configure(text='''Wyznacz''')

        self.designate_imp_btn = LeftMenuButton(self)
        self.designate_imp_btn.grid(**self.grid_config)
        self.designate_imp_btn.configure(text='''Impuls jednostkowy''')

        self.designate_An_btn = LeftMenuButton(self)
        self.designate_An_btn.grid(**self.grid_config)
        self.designate_An_btn.configure(text='''Współczynniki A i n prawa szybkości spalania''')

        self.designate_engine_para_btn = LeftMenuButton(self)
        self.designate_engine_para_btn.grid(**self.grid_config)
        self.designate_engine_para_btn.configure(text='''Współczynniki strat gazo-
dynamicznych i cieplnych''')
