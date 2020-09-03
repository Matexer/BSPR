import tkinter as tk
from .tree_list import TreeList
from .plots import PlotFrame
from .btns import Button


class ChooseList(TreeList):
    def __init__(self, top):
        self.checked_img = tk.PhotoImage(file='graphic/checked.gif')
        self.unchecked_img = tk.PhotoImage(file='graphic/unchecked.gif')
        super().__init__(top)

        self.plot_frame = PlotFrame(self)
        self.plot_frame.hide_toolbar()

        self.plot_frame.pack(side="left", fill='both')
        self.tree.pack(side="right", fill='both')

    def create_btns_container(self):
        container = tk.Frame(self)
        btns = []
        btn_labels = ("Edytuj wybrany", "Ustaw t chwilowe", "Wybierz wszystkie")
        for btn_label in btn_labels:
            btn = tk.Frame(container, text=btn_label)
            btn.pack(side="left")
            btns.append(btn)
        btns[-1].pack(side="right")
