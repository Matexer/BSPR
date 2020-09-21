from typing import Iterable, NewType, Tuple
import tkinter as tk
from matplotlib import pyplot
from .scrolled_frame import ScrolledFrameTemplate

Table = NewType("Table")


class ResultsFrameTemplate(ScrolledFrameTemplate):
    def __init__(self, top):
        super().__init__(top)

    def create_table(
            self, columns: Iterable, content: Iterable) \
            -> Table:
        ...

    def create_plot(self):
        ...