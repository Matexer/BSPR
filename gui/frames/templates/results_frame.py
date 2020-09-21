from typing import Iterable, NewType, Tuple
from gui.elements import PlotFigureFrame
from .scrolled_frame import ScrolledFrameTemplate


class ResultsFrameTemplate(ScrolledFrameTemplate):
    def __init__(self, top):
        super().__init__(top)

    def create_table(
            self, columns: Iterable, content: Iterable) \
            -> int:
        ...

    def create_plot(self, *args, **kwargs) -> PlotFigureFrame:
        ...
