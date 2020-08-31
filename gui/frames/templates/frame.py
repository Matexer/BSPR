import tkinter as tk
from gui.elements import *
from gui.configure import TL_BG


class FrameTemplate(tk.Frame):
    def __init__(self, top, *args, **kw):
        super().__init__(top, *args, **kw)
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
