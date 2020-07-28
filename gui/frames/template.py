import tkinter as tk
from gui.elements import TitleLabel, SubtitleLabel, InputTable


class TemplateFrame(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)

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