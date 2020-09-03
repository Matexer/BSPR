import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from gui.configure import TK_COLOR, T0_COLOR, TC_COLOR


class PlotFrame(tk.Frame):
    plot_fig_size = (10, 4)

    def __init__(self, top):
        super().__init__(top)
        self.plot, self.toolbar = self.create_plot()

    def create_plot(self):
        fig = Figure(figsize=self.plot_fig_size, dpi=100)
        self.canvas = canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=1, padx=10)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        toolbar.pack(side="top", fill="both", expand=1, padx=10)

        plot = fig.add_subplot(111)
        fig.subplots_adjust(left=0.08, bottom=0.12,
                            right=0.99, top=0.99)
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
        multiplier = tk.Entry(container, width=2)

        set_t0_btn.pack(side="left")
        set_tk_btn.pack(side="left")
        set_tc_btn.pack(side="left")
        fix_plot_btn.pack(side="left", padx=5)
        multiplier_label.pack(side="left", padx=5)
        multiplier.pack(side="left")
        return container, (set_t0_btn, set_tk_btn, set_tc_btn,
                           fix_plot_btn, multiplier)
