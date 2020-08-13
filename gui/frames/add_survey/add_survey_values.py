from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
from gui.frames.base import BaseFrame


class AddSurveyValuesBaseFrame(BaseFrame):
    def __init__(self, top):
        super().__init__(top)
        self.raw_values = None
        self.create_head_section()
        self.create_body_section()
        self.adjust_plot()

    def create_head_section(self):
        self.title = self.create_title('')
        self.title.pack(side="top", fill="x")

    def create_body_section(self):
        canvas_container, canvas, scroll = self.create_scrolled_section(self)
        self.create_plot_section(canvas, scroll)
        btns_container, self.down_nav_widgets = self.create_down_nav_container()

        canvas_container.pack(side="top", fill="both", expand=1)
        btns_container.pack(side="top", fill="x")

    @staticmethod
    def create_scrolled_section(top):
        canvas_container = tk.Frame(top, background="yellow")
        scroll = tk.Scrollbar(canvas_container, orient=tk.VERTICAL)
        scroll.pack(side='right', fill='y')
        canvas = tk.Canvas(canvas_container)
        # canvas['yscrollcommand'] = scroll.set
        scroll['command'] = canvas.yview
        canvas_container.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.pack(side="left", fill="both", expand=1)
        return canvas_container, canvas, scroll

    def create_plot_section(self, top, scroll):
        plot_container, self.survey_plot = self.create_plot_container(top)
        top.create_window((0, 0), window=plot_container, anchor="nw")
        top.configure(yscrollcommand=scroll.set)

    def create_plot_container(self, top, size=(10, 4)):
        plot_container = tk.Frame(top)
        fig = Figure(figsize=size, dpi=100)

        canvas = FigureCanvasTkAgg(fig, master=plot_container)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=1, padx=10)

        toolbar = NavigationToolbar2Tk(canvas, plot_container)
        toolbar.update()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=1, padx=10)

        survey_plot = fig.add_subplot(111)
        fig.subplots_adjust(left=0.08,
                            bottom=0.12,
                            right=0.99,
                            top=0.99)
        return plot_container, survey_plot

    def set_raw_values(self, values):
        self.raw_values = values

    def adjust_plot(self):
        pass


class AddSurveyPressureValuesFrame(AddSurveyValuesBaseFrame):
    def __init__(self, top):
        super().__init__(top)
        self.title.set_text("IMPORTOWANIE WARTOŚCI UZYSKANYCH Z POMIARU CiśNIENIA")

    def adjust_plot(self):
        super().adjust_plot()
        self.survey_plot.set_xlabel("Czas [ms]")
        self.survey_plot.set_ylabel("Ciśnienie [MPa]")


class AddSurveyThrustValuesFrame(AddSurveyValuesBaseFrame):
    def __init__(self, top):
        super().__init__(top)
        self.title.set_text("IMPORTOWANIE WARTOŚCI UZYSKANYCH Z POMIARU CIĄGU")

    def adjust_plot(self):
        super().adjust_plot()
        self.survey_plot.set_xlabel("Czas [ms]")
        self.survey_plot.set_ylabel("Siła ciągu [kN]")


class AddSurveyDoubleValuesFrame(AddSurveyValuesBaseFrame):
    def __init__(self, top):
        self.survey_plots = []
        super().__init__(top)
        self.title.set_text("IMPORTOWANIE WARTOŚCI UZYSKANYCH Z POMIARU CiśNIENIA I CIĄGU")

    def create_plot_section(self, top):
        plot_container1, survey_plot1 = self.create_plot_container(top)
        plot_container2, survey_plot2 = self.create_plot_container(top)

        self.survey_plots.append(survey_plot1)
        self.survey_plots.append(survey_plot2)

        plot_container1.pack(side="top", anchor="n")
        plot_container2.pack(side="top", anchor="n")

    def adjust_plot(self):
        self.survey_plots[0].set_xlabel("Czas [ms]")
        self.survey_plots[0].set_ylabel("Ciśnienie [MPa]")

        self.survey_plots[1].set_xlabel("Czas [ms]")
        self.survey_plots[1].set_ylabel("Siła ciągu [kN]")
