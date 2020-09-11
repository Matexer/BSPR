import tkinter as tk
from .tree_list import TreeList
from .plots import PlotFrame
from .btns import Button


class ChooseList(tk.Frame):
    PLOT_FIG_SIZE = 20, 4

    def __init__(self, top, *args, **kwargs):
        super().__init__(top, *args, **kwargs)

        self.tree_frame, self.mark_all_btn = self.__create_tree_frame()
        self.plot_frame, self.plot_buttons = self.__create_plot_frame()

        self.tree_frame.pack(side="left", fill="both")
        self.plot_frame.pack(side="right", fill="both")

        self.plots_data = []
        self.drawn_plots = []

    def __create_tree_frame(self):
        CheckTreeList = TreeList
        CheckTreeList.CHECK_OPTION = True
        tree_frame = CheckTreeList(self)
        tree_frame.tree.bind("<<TreeviewSelect>>", lambda e: self.__draw_plots())
        mark_all_btn = Button(tree_frame, text="Wybierz wszystkie",
                              command=lambda: tree_frame.toggle_all())
        mark_all_btn.pack(side="bottom", anchor="w")
        return tree_frame, mark_all_btn

    def __create_plot_frame(self):
        ExtendedPlotFrame = PlotFrame
        ExtendedPlotFrame.plot_fig_size = self.PLOT_FIG_SIZE
        plot_frame = ExtendedPlotFrame(self)
        plot_frame.hide_toolbar()
        plot_frame.canvas.get_tk_widget().pack_configure(padx=0)
        btn_container = tk.Frame(plot_frame)
        edit_btn = Button(btn_container, text="Edytuj wybrany", background="yellow")
        set_t_btn = Button(btn_container, text="Ustaw t chwilowe", background="orange")
        
        edit_btn.pack(side="right")
        set_t_btn.pack(side="right", padx=10)
        btn_container.pack(side="bottom", fill="both", padx=10)
        return plot_frame, (edit_btn, set_t_btn)

    def __draw_plots(self):
        for plot in self.drawn_plots:
            plot.remove()
        self.drawn_plots = []

        if not self.plots_data:
            raise AttributeError("Lack of data to plot")

        plot = self.plot_frame.plot
        selected_items = self.tree_frame.tree.selection()
        if not selected_items:
            return

        for item in selected_items:
            index = self.tree_frame.tree.index(item)
            data = self.plots_data[index]
            y_data = data[0]
            x_data = [data[1] * i for i in range(len(data) + 1)]
            self.drawn_plots.append(*plot.plot(x_data, y_data))

        self.plot_frame.canvas.draw()
