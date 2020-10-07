from typing import Tuple
import math
from ..templates import CalculationActTemplate
from ....core import An, AnOutplut
from ....gui.frames import ResultsFrame


class AnAct(CalculationActTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fuel_name = args[1]
        data = args[2]
        config = args[3]
        output = An(data, config).get_results()
        self.generate_report(self.frame, output)

    def generate_report(self, 
        frame: ResultsFrame, output: AnOutplut):
        title = frame.create_title(frame.interior, 
            f"WYNIKI OBLICZEŃ DLA PALIWA {self.fuel_name}")
        plotfig = frame.create_plot(frame.interior)
        plot = plotfig.add_subplot(111)
        plot.plot(*self.get_plot_cords(output))

        data = self.get_table_data(output)
        table = frame.create_table(frame.interior, data)

        title.pack(fill="both")
        plotfig.pack(pady=20)
        table.pack()

    @staticmethod
    def get_table_data(output: AnOutplut) -> Tuple[tuple, ...]:
        headings = ("Nr. pomiaru", "t0 [ms]", "tk [ms]", "tc [ms]", "Ipk")
        data = [(i, *item.times, item.Ipk) 
                for i, item in enumerate(output.surveys_details, start=1)]
        return tuple((headings, *data))

    @staticmethod
    def get_plot_cords(output: AnOutplut) -> Tuple[tuple, tuple]:
        xs = tuple(math.log(survey.p) for survey in output.surveys_details)
        ys = tuple(math.log(survey.u) for survey in output.surveys_details)
        return xs, ys