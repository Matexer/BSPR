import tkinter as tk
import tkinter.ttk as ttk
from .fuels_list import FuelsListFrame
from .templates import TemplateFrame


class SurveysListFrame(FuelsListFrame):
    def __init__(self, top):
        pass
        # TemplateFrame.__init__(self, top)
        #
        # title = self.create_title("LISTA POMIARÓW")
        # options_container = tk.Frame(self)
        # self.cboxs, self.buttons = self.create_options(options_container)
        # list_container = tk.Frame(self)
        # tree = self.create_list(list_container)
        #
        # self.buttons[0].configure(command=lambda: top.change_frame(3))
        #
        # title.pack(side="top", fill="x")
        # options_container.pack(side="top", fill="x", pady=5)
        # list_container.pack(side="top", fill="both", expand=1)
        #
        # top.update()
        # tree_width = top.winfo_width()
        # tree.set_columns(("Lp.",
        #                   "Śr. kryt. dyszy [mm]",
        #                   "Czas próbkowania [ms]",
        #                   "Masa paliwa [g]",
        #                   "Data"))
        # tree.set_columns_width(tree_width, (0.01, 0.225, 0.225, 0.225, 0.225))

    def create_options(self, top):
        cbox_container = tk.Frame(top)
        cboxs = self.create_cboxs(cbox_container)
        buttons_container = tk.Frame(top)
        buttons = self.create_btns(buttons_container)
        cbox_container.pack(side="left")
        buttons_container.pack(side="right")
        return cboxs, buttons

    @staticmethod
    def create_cboxs(top):
        left = tk.Frame(top)
        fuel_label = tk.Label(left)
        fuel_label.configure(text="Paliwo")
        fuel_cbox = ttk.Combobox(left)

        right = tk.Frame(top)
        type_label = tk.Label(right)
        type_label.configure(text="Rodzaj pomiaru")
        type_cbox = ttk.Combobox(right)

        fuel_label.pack(side="left")
        fuel_cbox.pack(side="left")
        type_label.pack(side="left")
        type_cbox.pack(side="left")

        left.pack(side="left")
        right.pack(side="left", padx=10)
        return fuel_cbox, type_cbox
