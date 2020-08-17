from gui.elements import AddSurveyValuesPlotFrame
from gui.frames.base import BaseFrame


class AddSurveyValuesBaseFrame(BaseFrame):
    def __init__(self, top):
        super().__init__(top)
        self.survey_plots = []
        self.plots_widgets = []
        self.create_head_section()
        self.create_body_section()
        self.adjust_plot()

    def create_head_section(self):
        self.title = self.create_title('')
        self.title.pack(side="top", fill="x")

    def create_body_section(self):
        scrolled_container, interior = self.create_scrolled_container(self)
        btns_container, self.down_nav_widgets = self.create_down_nav_container()
        self.create_plot_section(interior)

        scrolled_container.pack(side="top", fill="both", expand=1)
        btns_container.pack(side="bottom", fill="x")
        self.top.update_idletasks()

    def create_plot_section(self, top):
        plot_frame = AddSurveyValuesPlotFrame(top)
        self.survey_plots.append(plot_frame.plot)
        plot_frame.pack()

    def adjust_plot(self):
        for plot in self.survey_plots:
            plot.set_xlabel("Czas [ms]")


class AddSurveyPressureValuesFrame(AddSurveyValuesBaseFrame):
    def __init__(self, top):
        super().__init__(top)
        self.title.set_text("IMPORTOWANIE WARTOŚCI UZYSKANYCH Z POMIARU CiśNIENIA")

    def adjust_plot(self):
        super().adjust_plot()
        self.survey_plots[0].set_ylabel("Ciśnienie [MPa]")


class AddSurveyThrustValuesFrame(AddSurveyValuesBaseFrame):
    def __init__(self, top):
        super().__init__(top)
        self.title.set_text("IMPORTOWANIE WARTOŚCI UZYSKANYCH Z POMIARU CIĄGU")

    def adjust_plot(self):
        super().adjust_plot()
        self.survey_plots[0].set_ylabel("Siła ciągu [kN]")


class AddSurveyDoubleValuesFrame(AddSurveyValuesBaseFrame):
    def __init__(self, top):
        self.survey_plots = []
        super().__init__(top)
        self.title.set_text("IMPORTOWANIE WARTOŚCI UZYSKANYCH Z POMIARU CiśNIENIA I CIĄGU")

    def create_plot_section(self, top):
        for i in range(2):
            plot_frame = AddSurveyValuesPlotFrame(top)
            self.survey_plots.append(plot_frame.plot)
            plot_frame.pack(side="top", anchor="n", pady=20)

    def adjust_plot(self):
        super().adjust_plot()
        self.survey_plots[0].set_ylabel("Ciśnienie [MPa]")
        self.survey_plots[1].set_ylabel("Siła ciągu [kN]")
