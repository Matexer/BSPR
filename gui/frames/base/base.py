import tkinter as tk
from .scrolled import VerticalScrolledFrame
from gui.elements import *
from gui.configure import TL_BG


class BaseFrame(tk.Frame):
    def __init__(self, top):
        super().__init__(top)
        self.top = top
        self.messages = []

    def create_title(self, text):
        title = TitleLabel(self)
        title.configure(text=text)
        return title

    def create_subtitle(self, text):
        subtitle = SubtitleLabel(self)
        subtitle.configure(text=text)
        return subtitle

    def create_inputs_container(self, variables):
        inputs_container = tk.Frame(self)
        table = InputTable(inputs_container, variables)
        table.pack()
        return inputs_container, table

    def create_comment_container(self, width=100, height=8):
        comment_container = tk.Frame(self)
        comment = tk.Text(comment_container)
        comment.configure(width=width,
                          height=height)
        comment.pack(pady=5)
        return comment_container, comment

    def create_down_nav_container(self):
        btns_container = tk.Frame(self)
        btns_container.configure(bg=TL_BG)

        save_btn = SaveButton(btns_container)
        clear_btn = ClearButton(btns_container)
        cancel_btn = CancelButton(btns_container)

        message_label = MessageLabel(btns_container)
        message_label.configure(bg=TL_BG)
        self.messages.append(message_label)

        config = {"padx": 5, "pady": 5, "ipadx": 2, "ipady": 2}
        save_btn.pack(side="right", **config)
        cancel_btn.pack(side="left", **config)
        clear_btn.pack(side="left", **config)
        return btns_container, (save_btn, clear_btn, cancel_btn)

    def create_scrolled_container(self, top):
        container = VerticalScrolledFrame(top)
        interior = container.interior
        return container, interior
        # container = tk.Frame(top)
        #
        # vscrollbar = tk.Scrollbar(container, orient=tk.VERTICAL)
        # vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        # canvas = tk.Canvas(container, bd=0, highlightthickness=0,
        #                 yscrollcommand=vscrollbar.set)
        # canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        # vscrollbar.config(command=canvas.yview)
        #
        # canvas.xview_moveto(0)
        # canvas.yview_moveto(0)
        #
        # interior = interior = tk.Frame(canvas)
        # interior_id = canvas.create_window(0, 0, window=interior,
        #                                    anchor=tk.NW)
        #
        # def _configure_interior(event):
        #     size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
        #     canvas.config(scrollregion="0 0 %s %s" % size)
        #     if interior.winfo_reqwidth() != canvas.winfo_width():
        #         canvas.config(width=interior.winfo_reqwidth())
        # interior.bind('<Configure>', _configure_interior)
        #
        # def _configure_canvas(event):
        #     if interior.winfo_reqwidth() != canvas.winfo_width():
        #         canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        # canvas.bind('<Configure>', _configure_canvas)
        #
        # return container, interior

    def show_message(self, text, color="red", num=0):
        if self.messages:
            self.messages[num].set_text(text)
            self.messages[num].set_color(color)
            self.messages[num].pack(side="right", expand=1)

    def hide_message(self, num=0):
        if num >= 0:
            self.messages[num].pack_forget()
        else:
            for message in self.messages:
                message.pack_forget()
