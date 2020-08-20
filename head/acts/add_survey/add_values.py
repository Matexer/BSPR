from gui.configure import T0_COLOR, TK_COLOR, TC_COLOR
import tkinter as tk


class AddSurveyValuesAct:
    def __init__(self, top, import_frame, survey):
        self.top = top
        self.import_frame = import_frame
        self.survey = survey
        plot_frames = import_frame.plot_frames
        plots_widgets = [plot.widgets for plot in plot_frames]

        index = 0
        for plot_frame, data in zip(plot_frames, survey.values):
            plot_frame.plot.clear()
            self.prepare_plot(index, plot_frame, survey.sampling_time, data)
            plot_frame.canvas.draw()
            index += 1

    def prepare_plot(self, index, plot_frame, sampling_time, data):
        plot = plot_frame.plot
        plot_data = self.draw_plot(plot, sampling_time, data)[0]

        tk, t0, tc = self.get_times(data, sampling_time)
        self.survey.update({"t0": t0, "tk": tk, "tc": tc})
        t0_line = self.draw_line(plot, t0, color=T0_COLOR)
        tk_line = self.draw_line(plot, tk, color=TK_COLOR)
        tc_line = self.draw_line(plot, tc, color=TC_COLOR)

        plot.legend(["Wykes pomiaru", "t0 = %s ms" % t0,
                     "tk = %s ms" % tk, "tc = %s ms" % tc])

        _, xmax, _, ymax = plot.axis()
        plot.axis([0, xmax, 0, ymax])

        self.set_widgets(index, plot_frame, plot_data,
                         (t0_line, tk_line, tc_line))

    @staticmethod
    def draw_plot(plot, x, y):
        if not isinstance(x, (tuple, list)):
            x = [x * i for i in range(len(y))]
        return plot.plot(x, y)

    def set_widgets(self, i, plot_frame, plot_data, lines):
        set_t0_btn, set_tk_btn, set_tc_btn, fix_plot_btn, multiplier\
            = plot_frame.widgets

        set_t0_btn.configure(
            command=lambda: self.update_time(plot_frame, lines[0], "t0"))
        set_tk_btn.configure(
            command=lambda: self.update_time(plot_frame, lines[1], "tk"))
        set_tc_btn.configure(
            command=lambda: self.update_time(plot_frame, lines[2], "tc"))
        fix_plot_btn.configure(
            command=lambda: self.start_fix_survey(i, plot_frame, plot_data))

        value = tk.StringVar()
        value.set(1)
        value.trace(
            "w", lambda name, mode, index, value=value:
            self.change_multiplier_value(i, value, plot_frame, plot_data))

        multiplier.configure(textvariable=value)

    def change_multiplier_value(self, index, m_value, plot_frame, plot_data,):
        try:
            m_value = float(m_value.get())
        except ValueError:
            pass
        else:
            if 0 < m_value < 101:
                new_y = [val * m_value for val in self.survey.values[index]]
                plot_data.set_ydata(new_y)
                _, xmax, _, _ = plot_frame.plot.axis()
                y_max = max(new_y) * 1.05
                plot_frame.plot.axis([0, xmax, 0, y_max])
                plot_frame.canvas.draw()

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
        t0 = get_first_no_zero() * smp_time
        tc = get_last_zero() * smp_time             #last 0 value form right
        return tk, t0, tc

    @staticmethod
    def draw_line(plot, tk, color="red"):
        return plot.axvline(x=tk, color=color, linestyle="--")

    def update_time(self, plot_frame, time_line, time_name):
        plot_canvas = plot_frame.plot.figure.canvas

        def update_line(event):
            new_x = event.xdata
            if new_x:
                time_line.set_xdata(new_x)
                plot_frame.canvas.draw()
                self.survey.update({time_name: round(new_x, 2)})
                self.refresh_legend(plot_frame.plot)

        def start_updating():
            return plot_canvas.mpl_connect("motion_notify_event",
                                           lambda event: update_line(event))

        def end_updating():
            plot_canvas.mpl_disconnect(connection_id)

        connection_id = start_updating()
        plot_canvas.mpl_connect("button_press_event",
                                lambda event: end_updating())

    def refresh_legend(self, plot):
        plot.legend(["Wykes pomiaru", "t0 = %s ms" % self.survey.t0,
                     "tk = %s ms" % self.survey.tk, "tc = %s ms" % self.survey.tc])

    def start_fix_survey(self, i, plot_frame, plot_data):
        plot_canvas = plot_frame.plot.figure.canvas
        first_line = None

        def set_line(event, color="red"):
             return plot_frame.plot.axvline(x=event.xdata, color=color, linestyle=":")

        def try_fix(event):
            nonlocal first_line
            if first_line == None:
                first_line = set_line(event)
                plot_frame.canvas.draw()
            else:
                self.fix_survey(i, first_line.get_xdata()[0], event.xdata,
                                plot_frame, plot_data)
                plot_frame.plot.lines.remove(first_line)
                plot_frame.canvas.draw()
                plot_canvas.mpl_disconnect(connection_id)
                first_line = None

        connection_id = plot_canvas.mpl_connect("button_press_event",
                                                lambda event: try_fix(event))

    def fix_survey(self, i, x1, x2, plot_frame, plot_data):
        y_data = plot_data.get_ydata()

        x = [x1, x2]
        t1 = min(x)
        t2 = max(x)

        index1 = int(t1 // self.survey.sampling_time)
        index2 = int(t2 // self.survey.sampling_time)
        delta_x = abs(index1 - index2)

        y1 = y_data[index1]
        y2 = y_data[index2]
        delta_y = y2 - y1

        step = delta_y / delta_x

        change = 0
        for index in range(index1, index2+1):
            y_data[index] = y1 + change
            change += step

        plot_data.set_ydata(y_data)
        plot_frame.canvas.draw()
        self.survey.values[i] = y_data
