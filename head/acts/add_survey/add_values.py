from gui.configure import T0_COLOR, TK_COLOR, TC_COLOR


class AddSurveyValuesAct:
    def __init__(self, top, import_frame, raw_survey_values, sampling_time):
        self.top = top
        plot_frames = import_frame.plot_frames
        self.import_frame = import_frame
        plots_widgets = [plot.widgets for plot in plot_frames]

        for plot_frame, data in zip(plot_frames, raw_survey_values):
            self.prepare_plot(plot_frame, sampling_time, data)

    def prepare_plot(self, plot_frame, sampling_time, data):
        plot = plot_frame.plot
        plot_frame.draw_plot(sampling_time, data)
        tk, t0, tc = self.get_times(data, sampling_time)
        t0_line = self.draw_line(plot, t0, color=T0_COLOR)
        tk_line = self.draw_line(plot, tk, color=TK_COLOR)
        tc_line = self.draw_line(plot, tc, color=TC_COLOR)
        plot.legend(["Wykes pomiaru", "t0 = %s ms" % t0,
                     "tk = %s ms" % tk, "tc = %s ms" % tc])
        _, xmax, _, ymax = plot.axis()
        plot.axis([0, xmax, 0, ymax])
        self.set_tk(plot_frame, tk_line)

    @staticmethod
    def get_times(data, smp_time):
        def get_first_no_zero():
            for i, value in enumerate(data):
                if value:
                    first_no_zero = i
                    first_zero = first_no_zero - 1
                    if first_zero > -1:
                        return first_zero
                    else:
                        return first_no_zero
            return 0

        def get_last_zero():
            length = len(data)
            for i in range(- 1, - length, -1):
                if data[i]:
                    first_no_zero = i + length
                    last_zero = first_no_zero + 1
                    if last_zero < length:
                        return last_zero
                    else:
                        return first_no_zero
            return length - 1

        tk = data.index(max(data)) * smp_time       #highest value
        t0 = get_first_no_zero() * smp_time         #first 0 value from left
        tc = get_last_zero() * smp_time             #last 0 value form right
        return tk, t0, tc

    @staticmethod
    def draw_line(plot, tk, color="red"):
        return plot.axvline(x=tk, color=color, linestyle="--")

    def set_tk(self, plot_frame, tk_line):
        pass
        plot_frame.plot.figure.canvas.mpl_connect("button_press_event",
                                                  lambda event: self.update_tk(event, plot_frame, tk_line))

        # plot.figure.canvas.mpl_connect("motion_notify_event", None)

    def update_tk(self, event, plot_frame, tk_line):
        new_x = event.xdata
        if new_x:
            tk_line.set_xdata(new_x)
            self.import_frame.scrolled_container.update()
