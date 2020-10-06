from typing import Iterable
from ..elements import PlotFigureFrame
from .templates.scrolled_frame import ScrolledFrameTemplate
from ..elements import TableFrame


class ResultsFrame(ScrolledFrameTemplate):
    def __init__(self, top):
        super().__init__(top)

    @staticmethod
    def create_table(top, data: Iterable[Iterable], *args, **kwargs)\
            -> TableFrame:
        return TableFrame(top, data, *args, **kwargs)

    @staticmethod
    def create_plot(top, *args, **kwargs) -> PlotFigureFrame:
        return PlotFigureFrame(top, *args, **kwargs)
