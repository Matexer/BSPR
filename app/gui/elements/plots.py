import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure, SubplotBase
from ..configure import TK_COLOR, T0_COLOR, TC_COLOR
from typing import Tuple, Literal, Union


Boolean = Literal[True, False]


class PlotFigureFrame(tk.Frame):
    FIGSIZE: Tuple[int] = (10, 4)
    DPI: int = 100
    TOOLBAR: Boolean = True
    SUBPLOTS_ADJUST: dict = {"left": 0.08, "bottom": 0.12,
                             "right": 0.99, "top": 0.99}

    def __init__(self, *args, **kwargs):
        self.__update_vars(kwargs)
        super().__init__(*args, **kwargs)
        self.canvas, self.figure = self.__create_figure()

    def add_subplot(self, position: Union[int, Tuple[int]])\
        -> SubplotBase:
        if isinstance(position, tuple):
            return self.figure.add_subplot(*position)
        return self.figure.add_subplot(position)

    def __update_vars(self, kwargs: dict):
        variables = ("figsize", "dpi",
                     "toolbar", "subplot_adjust")

        for key in variables:
            if key in kwargs:
                self.__setattr__(key.upper(), kwargs.pop(key))

    def __create_figure(self) -> Tuple[FigureCanvasTkAgg, Figure]:
        fig = Figure(figsize=self.FIGSIZE, dpi=self.DPI)
        fig.subplots_adjust(**self.SUBPLOTS_ADJUST)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack(
            side="top", fill="both", expand=1, padx=10)

        if self.TOOLBAR:
            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            toolbar.pack(
                side="top", fill="both", expand=1, padx=10)
        canvas.draw()
        return canvas, fig


class PlotFrame(tk.Frame):
    PLOT_FIG_SIZE = (20, 4)

    def __init__(self, top):
        super().__init__(top)
        self.plot, self.toolbar = self.create_plot()
        self.canvas: FigureCanvasTkAgg

    def create_plot(self):
        self.fig = fig = Figure(figsize=self.PLOT_FIG_SIZE, dpi=100)
        self.canvas = canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=1, padx=10)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        toolbar.pack(side="top", fill="both", expand=1, padx=10)

        plot = fig.add_subplot(111)
        fig.subplots_adjust(left=0.086, bottom=0.12,
                            right=0.99, top=0.936)
        return plot, toolbar

    def show_toolbar(self):
        self.toolbar.pack(side="top", fill="both", expand=1, padx=10)

    def hide_toolbar(self):
        self.toolbar.pack_forget()


class AddSurveyValuesPlotFrame(PlotFrame):
    def __init__(self, top):
        super().__init__(top)
        self.lines = {}

    def create_plot(self):
        plot, toolbar = super().create_plot()
        correction_container, widgets = self.create_correction_section(self)
        correction_container.pack(side="bottom", fill="x", padx=10)
        self.widgets = widgets
        return plot, toolbar

    @staticmethod
    def create_correction_section(top):
        container = tk.Frame(top)
        set_t0_btn = tk.Button(container, text="Ustaw t0", background=T0_COLOR)
        set_tk_btn = tk.Button(container, text="Ustaw tk", background=TK_COLOR)
        set_tc_btn = tk.Button(container, text="Ustaw tc", background=TC_COLOR)
        fix_plot_btn = tk.Button(container, text="Napraw pomiar")
        multiplier_label = tk.Label(container, text="Mnożnik wartości")
        multiplier = tk.Entry(container, width=6)

        set_t0_btn.pack(side="left")
        set_tk_btn.pack(side="left")
        set_tc_btn.pack(side="left")
        fix_plot_btn.pack(side="left", padx=5)
        multiplier_label.pack(side="left", padx=5)
        multiplier.pack(side="left")
        return container, (set_t0_btn, set_tk_btn, set_tc_btn,
                           fix_plot_btn, multiplier)
