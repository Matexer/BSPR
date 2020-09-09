import tkinter as tk
from .tree_list import TreeList
from .plots import PlotFrame
from .btns import Button


class ChooseList(tk.Frame):
    PLOT_FIG_SIZE = 20, 4

    def __init__(self, top, *args, **kwargs):
        super().__init__(top, *args, **kwargs)
        self.checked_img = tk.PhotoImage(file='graphic/checked.gif')
        self.unchecked_img = tk.PhotoImage(file='graphic/unchecked.gif')

        self.tree_frame, self.mark_all_btn = self.__create_tree_frame()
        self.plot_frame, self.plot_buttons = self.__create_plot_frame()

        self.tree_frame.pack(side="left", fill="both")
        self.plot_frame.pack(side="right", fill="both")

        self.chosen_items_ids = []

    def __create_tree_frame(self):
        tree_frame = TreeList(self)
        mark_all_btn = Button(tree_frame, text="Wybierz wszystkie")
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

    def __toggle_item(self, event):
        item = self.tree_frame.tree.identify("item", event.x, event.y)
        index = self.tree_frame.tree.index(item)
        if index in self.chosen_items_ids:
            self.chosen_items_ids.remove(index)
            item["image"] = self.unchecked_img
        else:
            self.chosen_items_ids.append(index)
            item["image"] = self.checked_img
