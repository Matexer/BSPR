from typing import Iterable
from ...elements import PlotFigureFrame
from .scrolled_frame import ScrolledFrameTemplate
from ...elements import TableFrame


class ResultsFrame(ScrolledFrameTemplate):
    def __init__(self, top):
        super().__init__(top)
        self.generate_structure()

    @staticmethod
    def create_table(top, data: Iterable[Iterable], *args, **kwargs)\
            -> TableFrame:
        return TableFrame(top, data, *args, **kwargs)

    @staticmethod
    def create_plot(top, *args, **kwargs) -> PlotFigureFrame:
        return PlotFigureFrame(top, *args, **kwargs)

    def generate_structure(self):
        title = self.create_title(self.interior, "WYNIKI OBLICZEŃ")
        title.pack()
        table_data = (("Head 1", "Head 2", "Head 3", "Head 4"),
                      (1, 2, 3, 5),
                      (4, "0000000000000000\n0\n0\n00000000", 6, 7),
                      (7, 8, 9, 9),
                      (7, 8, 9, 9),
                      (7, 8, 9, 9))
        table = self.create_table(self.interior, table_data)
        table.pack(fill="both", expand=1, anchor="center")
        plot = self.create_plot(self.interior)
        plot.pack()
