import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


class PlotFrame(tk.Frame):
    def __init__(self, top):
        super().__init__(top)
        self.plot, self.toolbar = self.create_plot()

    def create_plot(self, size=(10, 4)):
        fig = Figure(figsize=size, dpi=100)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=1, padx=10)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        toolbar.pack(side="top", fill="both", expand=1, padx=10)

        plot = fig.add_subplot(111)
        fig.subplots_adjust(left=0.08, bottom=0.12,
                            right=0.99, top=0.99)
        return plot, toolbar

    def draw_plot(self, x, y):
        if not isinstance(x, (tuple, list)):
            x = [x * i for i in range(len(y))]
        self.plot.plot(x, y)

    def show_toolbar(self):
        self.toolbar.pack(side="top", fill="both", expand=1, padx=10)

    def hide_toolbar(self):
        self.toolbar.pack_forget()


class AddSurveyValuesPlotFrame(PlotFrame):
    def __init__(self, top):
        super().__init__(top)

    def create_plot(self):
        plot, toolbar = super().create_plot()
        correction_container, widgets = self.create_correction_section(self)
        correction_container.pack(side="bottom", fill="x", padx=10)
        self.__setattr__("widgets", widgets)
        return plot, toolbar

    @staticmethod
    def create_correction_section(top):
        container = tk.Frame(top)
        set_tk_btn = tk.Button(container, text="Ustaw tk")
        fix_plot_btn = tk.Button(container, text="Napraw pomiar")
        multiplier_label = tk.Label(container, text="Mnożnik wartości")
        multiplier = tk.Entry(container, width=2)
        message = tk.Label(container)

        set_tk_btn.pack(side="left")
        fix_plot_btn.pack(side="left", padx=5)
        multiplier_label.pack(side="left", padx=5)
        multiplier.pack(side="left")
        return container, (set_tk_btn, fix_plot_btn, multiplier, message)