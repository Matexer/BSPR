import tkinter as tk
from .tree_list import TreeList
from .plots import PlotFrame
from .btns import Button
from typing import Tuple, AnyStr


class CheckTreeList(TreeList):
    CHECK_OPTION = True
    AUTO_NUMBERING = True


class ChooseList(tk.Frame):
    PLOT_FIG_SIZE = 20, 4

    def __init__(self, top, *args, **kwargs):
        super().__init__(top, *args, **kwargs)

        self.tree_frame, self.mark_all_btn = self.__create_tree_frame(self)
        self.plot_frame, self.plot_buttons = self.__create_plot_frame(self)
        self.comment_frame, self.comment = self.__create_comment_frame(self)

        self.tree_frame.pack(side="left", fill="y")
        self.plot_frame.pack(side="right", fill="both")
        self.comment_frame.pack(side="bottom", fill="x")

        self.plots_data = Tuple[Tuple, int, AnyStr]
        self.surveys_t_lines = []
        self.drawn_plots = []

    def set_plots_data(self, data: Tuple[Tuple, int, AnyStr]):
        self.plot_frame.plot.lines = []
        self.plots_data = data
        max_val_time = \
            lambda plot_data: plot_data[0].index(max(plot_data[0])) * plot_data[1]
        self.surveys_t_lines = \
            [self.__draw_line(x, hidden=True) for x in (max_val_time(d) for d in data)]
        self.hide_lines()

    def hide_lines(self):
        for line in self.surveys_t_lines:
            if line:
                line.set_alpha(0)
        self.plot_frame.canvas.draw()

    def clean(self):
        self.tree_frame.clean()
        self.plot_frame.plot.lines = []
        self.plot_frame.plot.legend()
        self.comment.configure(text="")
        self.plot_frame.canvas.draw()

    def __draw_line(self, x, *, hidden=False):
        a = 0 if hidden else 1
        line = self.plot_frame.plot.axvline(x=x, color="orange", alpha=a, linestyle="--")
        self.plot_frame.plot.figure.canvas.draw()
        return line

    def __show_line(self, index):
        line = self.surveys_t_lines[index]
        if line:
            line.set_alpha(1)
        self.plot_frame.canvas.draw()

    def __create_tree_frame(self, top):
        tree_frame = CheckTreeList(top)
        tree_frame.tree.bind("<<TreeviewSelect>>", lambda e: self.__show_surveys())
        mark_all_btn = Button(tree_frame, text="Wybierz wszystkie",
                              command=lambda: tree_frame.toggle_all())
        mark_all_btn.pack(side="bottom", anchor="w")
        return tree_frame, mark_all_btn

    def __create_plot_frame(self, top):
        ExtendedPlotFrame = PlotFrame
        ExtendedPlotFrame.plot_fig_size = self.PLOT_FIG_SIZE
        plot_frame = ExtendedPlotFrame(top)
        plot_frame.hide_toolbar()
        plot_frame.canvas.get_tk_widget().pack_configure(padx=0)
        btn_container = tk.Frame(plot_frame)
        edit_btn = Button(btn_container, text="Edytuj wybrany", background="yellow")
        set_t_btn = Button(btn_container, text="Ustaw t chwilowe", background="orange",
                           command=lambda: self.__set_t())
        
        edit_btn.pack(side="right")
        set_t_btn.pack(side="right", padx=10)
        btn_container.pack(side="bottom", fill="both", padx=10)
        return plot_frame, (edit_btn, set_t_btn)

    @staticmethod
    def __create_comment_frame(top):
        container = tk.Frame(top)
        title = tk.Label(container, text="KOMENTARZ: ")
        content = tk.Label(container)
        title.pack(anchor="w")
        content.pack(anchor="w")
        container.pack(fill="x", padx=10)
        return container, content

    def __show_surveys(self):
        if not self.plots_data:
            raise AttributeError("Lack of plot's data")

        plot = self.plot_frame.plot
        selected_items = self.tree_frame.tree.selection()

        ids = [self.tree_frame.tree.index(i) for i in selected_items]

        if not selected_items:
            return

        self.__clean_plots()
        self.__draw_plots(plot, ids)
        self.__show_comment(self.plots_data[ids[0]][2])

    def __clean_plots(self):
        for plot in self.drawn_plots:
            plot.remove()
        self.drawn_plots = []

    def __draw_plots(self, plot, ids):
        self.hide_lines()
        showed_plots_times = set()

        max_x = 0
        max_y = 0

        for index in ids:
            data = self.plots_data[index]
            y_data = data[0]
            max_y = max(y_data) if max(y_data) > max_y else max_y
            x_data = [data[1] * i for i in range(len(y_data))]
            max_x = x_data[-1] if x_data[-1] > max_x else max_x
            self.drawn_plots.append(*plot.plot(x_data, y_data))
            time = self.surveys_t_lines[index].get_xdata()
            time = time[0] if isinstance(time, list) else time
            showed_plots_times.add(time)

        if len(showed_plots_times) == 1:
            self.__show_line(ids[0])
            self.__refresh_legend(ids[0])
        else:
            self.__refresh_legend()

        self.plot_frame.plot.axis([0, max_x*1.05, 0, max_y*1.05])
        self.plot_frame.canvas.draw()

    def __refresh_legend(self, timeline_id=-1):
        plots = [p for p in self.drawn_plots]
        numbers = list(range(1, len(self.drawn_plots) + 1))

        if timeline_id >= 0:
            line = self.surveys_t_lines[timeline_id]
            x_val = line.get_xdata()
            x_val = x_val[0] if isinstance(x_val, list) else x_val
            plots.append(line)
            numbers.append("t = {:.2f} ms".format(x_val))

        self.plot_frame.plot.legend(plots, numbers)

    def __show_comment(self, text):
        self.comment.configure(text=text)

    def __set_t(self):
        p_canvas = self.plot_frame.plot.figure.canvas
        selected_items = self.tree_frame.tree.selection()
        if not (selected_items and self.plots_data):
            return

        ids = [self.tree_frame.tree.index(i) for i in selected_items]
        set_x = None
        LINES_SET = False

        def start_moving_line():
            self.__show_line(ids[0])
            return p_canvas.mpl_connect("motion_notify_event",
                                        lambda event: move_line(event))

        def move_line(event):
            new_x = event.xdata
            if not new_x:
                return
            self.surveys_t_lines[ids[0]].set_xdata(new_x)
            p_canvas.draw()
            nonlocal set_x
            set_x = new_x
            self.__refresh_legend(ids[0])

        def set_rest_lines():
            for index in ids[1:]:
                if set_x:
                    self.surveys_t_lines[index].set_xdata(set_x)
            p_canvas.draw()

        def stop_moving_line():
            p_canvas.mpl_disconnect(event_id)
            nonlocal LINES_SET
            if not LINES_SET:
                LINES_SET = True
                set_rest_lines()

        event_id = start_moving_line()
        p_canvas.mpl_connect("button_press_event",
                             lambda event: stop_moving_line())
