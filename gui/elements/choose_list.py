import tkinter as tk
from .tree_list import TreeList
from .plots import PlotFrame
from .btns import Button
from typing import Tuple, AnyStr


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
        self.plots_data = data
        self.surveys_t_lines = [None] * len(data)

    def __create_tree_frame(self, top):
        CheckTreeList = TreeList
        CheckTreeList.CHECK_OPTION = True
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
        self.show_line(ids[0])
        for index in ids:
            data = self.plots_data[index]
            y_data = data[0]
            x_data = [data[1] * i for i in range(len(y_data))]
            self.drawn_plots.append(*plot.plot(x_data, y_data))

        self.plot_frame.canvas.draw()

    def __show_comment(self, text):
        self.comment.configure(text=text)

    def __set_t(self):
        p_canvas = self.plot_frame.plot.figure.canvas
        selected_item = self.tree_frame.tree.selection()
        if selected_item and self.plots_data:
            selected_item = selected_item[0]
        else:
            return

        index = self.tree_frame.tree.index(selected_item)

        def start_moving_line():
            return p_canvas.mpl_connect("motion_notify_event",
                                        lambda event: move_line(event))

        def move_line(event):
            new_x = event.xdata
            if not new_x:
                return
            self.surveys_t_lines[index].set_xdata(new_x)
            p_canvas.draw()

        def stop_moving_line():
            p_canvas.mpl_disconnect(event_id)

        if not self.surveys_t_lines[index]:
            x = self.plots_data[index][0].index(max(self.plots_data[index][0])) *\
                self.plots_data[index][1]
            self.surveys_t_lines[index] = self.draw_line(x)

        event_id = start_moving_line()
        p_canvas.mpl_connect("button_press_event",
                             lambda event: stop_moving_line())

    def draw_line(self, x):
        line = self.plot_frame.plot.axvline(x=x, color="orange", linestyle="--")
        self.plot_frame.plot.figure.canvas.draw()
        return line

    def hide_lines(self):
        for line in self.surveys_t_lines:
            if line:
                line.set_alpha(0)

    def show_line(self, index):
        line = self.surveys_t_lines[index]
        if line:
            line.set_alpha(1)
