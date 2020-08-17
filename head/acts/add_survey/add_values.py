class AddSurveyValuesAct:
    def __init__(self, top, import_frame, raw_survey_values, sampling_time):
        self.top = top
        plots = import_frame.survey_plots
        plots_widgets = import_frame.plots_widgets

        for plot, data in zip(plots, raw_survey_values):
            self.set_plot_data(plot, data, sampling_time)
            tk = self.get_tk(data, sampling_time)
            self.set_tk(plot, tk)
            self.set_legend(plot, tk)


    @staticmethod
    def set_plot_data(plot, data, smp_time):
        t = [smp_time * i for i in range(len(data))]
        plot.plot(t, data)

    @staticmethod
    def get_tk(data, smp_time):
        i = data.index(max(data))
        time = i * smp_time
        return time

    @staticmethod
    def set_tk(plot, tk):
        plot.axvline(x=tk, color="red")

    @staticmethod
    def set_legend(plot, tk):
        plot.legend(["Wykes pomiaru", "tk = %s ms"%tk])

    def set_buttons(self):
        for plot, widgets in zip(self.frame.survey_plots, self.frame.plots_widgets):
            set_tk_btn = widgets[0]
            fix_plot_btn = widgets[1]
            set_tk_btn.configure(command=lambda: 5)
            fix_plot_btn.configure(command=lambda: 5)
