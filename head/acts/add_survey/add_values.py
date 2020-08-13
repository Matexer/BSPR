class AddSurveyValuesAct:
    def __init__(self, top, import_frame, raw_survey_values, sampling_time):
        self.top = top
        self.frame = import_frame
        if isinstance(raw_survey_values[0], (tuple, list)):
            for data, plot in zip(raw_survey_values, import_frame.survey_plots):
                self.set_plot_data(plot, data, sampling_time)
                tk = self.get_tk(data, sampling_time)
                plot.axvline(x=tk, color="red")
                plot.legend(["Wykes pomiaru", "tk = %s ms"%tk])
        else:
            self.set_plot_data(import_frame.survey_plot, raw_survey_values, sampling_time)
            tk = self.get_tk(raw_survey_values, sampling_time)
            import_frame.survey_plot.axvline(x=tk, color="red")
            import_frame.survey_plot.legend(["Wykes pomiaru", "tk"])

    @staticmethod
    def set_plot_data(plot, data, smp_time):
        t = [smp_time * i for i in range(len(data))]
        plot.plot(t, data)

    def get_tk(self, data, smp_time):
        i = data.index(max(data))
        time = i * smp_time
        return time

    def set_tk(self, plot, tk):
        pass
