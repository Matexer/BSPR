from gui.elements import AddSurveyValuesPlotFrame
from ..templates import FrameTemplate, ScrolledFrameTemplate


class AddSurveyValuesBaseFrameTemplate(FrameTemplate):
    def __init__(self, top):
        super().__init__(top)
        self.plot_frames = []
        self.create_head_section()
        self.create_body_section()
        self.adjust_plot()

    def create_head_section(self):
        self.title = self.create_title(self, '')
        self.title.pack(side="top", fill="x")

    def create_body_section(self):
        self.scrolled_container, interior = self.create_scrolled_container(self)
        nav_container, self.down_nav_widgets = self.create_down_nav_container(self)
        self.create_plot_section(interior)

        clear_btn, cancel_btn = self.down_nav_widgets[1:3]
        clear_btn.config(text="RESET")
        cancel_btn.pack_forget()

        self.scrolled_container.pack(side="top", fill="both", expand=1)
        nav_container.pack(side="bottom", fill="x")
        self.top.update_idletasks()
        self.scrolled_container.update()

    def create_scrolled_container(self, top):
        container = ScrolledFrameTemplate(top)
        interior = container.interior
        return container, interior

    def create_plot_section(self, top):
        plot_frame = AddSurveyValuesPlotFrame(top)
        self.plot_frames.append(plot_frame)
        plot_frame.pack()

    def adjust_plot(self):
        for frame in self.plot_frames:
            frame.plot.set_xlabel("Czas [ms]")


class AddSurveyPressureValuesFrame(AddSurveyValuesBaseFrameTemplate):
    def __init__(self, top):
        super().__init__(top)
        self.title.set_text("IMPORTOWANIE WARTOŚCI UZYSKANYCH Z POMIARU CiśNIENIA")

    def adjust_plot(self):
        super().adjust_plot()
        self.plot_frames[0].plot.set_ylabel("Ciśnienie [MPa]")


class AddSurveyThrustValuesFrame(AddSurveyValuesBaseFrameTemplate):
    def __init__(self, top):
        super().__init__(top)
        self.title.set_text("IMPORTOWANIE WARTOŚCI UZYSKANYCH Z POMIARU CIĄGU")

    def adjust_plot(self):
        super().adjust_plot()
        self.plot_frames[0].plot.set_ylabel("Siła ciągu [kN]")


class AddSurveyDoubleValuesFrame(AddSurveyValuesBaseFrameTemplate):
    def __init__(self, top):
        super().__init__(top)
        self.title.set_text("IMPORTOWANIE WARTOŚCI UZYSKANYCH Z POMIARU CiśNIENIA I CIĄGU")

    def create_plot_section(self, top):
        for i in range(2):
            plot_frame = AddSurveyValuesPlotFrame(top)
            self.plot_frames.append(plot_frame)
            plot_frame.pack(side="top", anchor="n", pady=20)

    def adjust_plot(self):
        super().adjust_plot()
        self.plot_frames[0].plot.set_ylabel("Ciśnienie [MPa]")
        self.plot_frames[1].plot.set_ylabel("Siła ciągu [kN]")
