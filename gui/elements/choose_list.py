import tkinter as tk
from .tree_list import TreeList
from .plots import PlotFrame
from .btns import Button


class ChooseList(tk.Frame):
    def __init__(self, top, *args, **kwargs):
        super().__init__(top, *args, **kwargs)
        self.checked_img = tk.PhotoImage(file='graphic/checked.gif')
        self.unchecked_img = tk.PhotoImage(file='graphic/unchecked.gif')

        self.tree_frame, self.mark_all_btn = self.create_tree_frame()
        self.plot_frame, self.plot_buttons = self.create_plot_frame()

        self.tree_frame.pack(side="right", fill="both")
        self.plot_frame.pack(side="left", fill="both")

    def create_tree_frame(self):
        tree_frame = TreeList(self)
        mark_all_btn = Button(tree_frame, text="Wybierz wszystkie")
        mark_all_btn.pack(side="bottom", anchor="w")
        return tree_frame, mark_all_btn

    def create_plot_frame(self):
        plot_frame = PlotFrame(self)
        plot_frame.hide_toolbar()
        plot_frame.canvas.get_tk_widget().pack_configure(padx=0)
        btn_container = tk.Frame(plot_frame)
        edit_btn = Button(btn_container, text="Edytuj wybrany", background="yellow")
        set_t_btn = Button(btn_container, text="Ustaw t chwilowe", background="orange")
        edit_btn.pack(side="left")
        set_t_btn.pack(side="left", padx=10)
        btn_container.pack(side="bottom", fill="both")
        return plot_frame, (edit_btn, set_t_btn)
