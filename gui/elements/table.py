import tkinter as tk
from itertools import islice


class Element(tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Heading(Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(text="bold")


class TableFrame(tk.Frame):
    HEADING_COLORS = ("yellow", "pink")
    ROW_COLORS = (("green", "red", "gray"),
                  ("violet", "yellow", "blue"))
    HORIZONTAL = True

    def __init__(self, headings, data, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __create_table(self, size):
        ...

    def __create_headings(self, headings):
        ...

    def __create_row(self, data):
        ...

    def __create_column(self, data):
        ...

    def __prepare_data(self, data, chain_length):
        prepared_data = []
        for num, value in zip((i for i in range(5)) ,data):

