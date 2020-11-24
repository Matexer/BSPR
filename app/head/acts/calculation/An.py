from typing import Tuple, List
import math
import tkinter as tk
from ..templates import CalculationActTemplate
from ....core import An, AnOutplut
from ....gui.frames import ResultsFrame


class AnAct(CalculationActTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fuel_name = args[1]
        data = args[2]
        self.config = args[3]
        output = An(data, self.config).get_results()
        self.generate_report(self.frame, output)

    def generate_report(self, 
        frame: ResultsFrame, output: AnOutplut):
        title = frame.create_title(frame.interior, 
            "WYNIKI OBLICZEŃ WSPÓŁCZYNNIKÓW A i n PRAWA "
            f"SZYBKOŚCI SPALANIA DLA PALIWA {self.fuel_name}")

        plotfig = self.draw_approx_plot(frame, output)

        final_output = tk.Label(frame.interior, text=f"A = {output.A:.3e} m/(s⋅Pa^n)\
            n = {output.n:.3g}", font=("bold", 20))

        data = self.get_table_data(output)
        table = frame.create_table(frame.interior, data)

        export_btn = frame.create_export_btn(frame.interior)

        title.pack(fill="both")
        plotfig.pack(expand=1, fill="both")
        final_output.pack(pady=10)
        table.pack()
        export_btn.pack(pady=5)

        data.append('')
        data.append(("A [m/(s⋅Pa^n)]", output.A, "n", output.n), )
        export_btn.configure(command=lambda: self.export_data(data))

    def get_table_data(self, output: AnOutplut)\
        -> List[tuple]:
        if self.config.calculation_method == 0: #average
            headings = ("Nr.\npomiaru", "p śr.\n[MPa]", "u śr.\n[mm/s]","t0\n[ms]", "tk\n[ms]", 
                "Ipk\n[MPa⋅s]", "Śr. kryt.\ndyszy [mm]", "Min. śr. kryt.\ndyszy [mm]")
            data = [(i, round(item.p/1000_000, 3), round(item.u*1000, 2), *item.times[:-1],
                round(item.Ipk/1000_000, 3), item.jet_d, round(item.d_min, 1))
                    for i, item in enumerate(output.surveys_details, start=1)]
            return list((headings, *data))
        
        headings = ("Nr.\npomiaru", "p chw.\n[MPa]", "u chw.\n[mm/s]","t0\n[ms]", "tk\n[ms]", 
            "Ipk\n[MPa⋅s]", "Śr. kryt.\ndyszy [mm]", "Min. śr. kryt.\ndyszy [mm]", "t chwil.\n[ms]")
        data = [(i, round(item.p/1000_000, 3), round(item.u*1000, 2), *item.times[:-1],
            round(item.Ipk/1000_000, 3), item.jet_d, round(item.d_min, 1),
            round(item.point_time,2))
                for i, item in enumerate(output.surveys_details, start=1)]
        return list((headings, *data))

    @staticmethod
    def get_plot_cords(output: AnOutplut)\
        -> Tuple[tuple, tuple]:
        xs = tuple(math.log(survey.p) for survey in output.surveys_details)
        ys = tuple(math.log(survey.u) for survey in output.surveys_details)
        return xs, ys

    def draw_approx_plot(self, frame, output):
        plotfig = frame.create_plot(frame.interior)
        plotfig.figure.subplots_adjust(left=0.095, top=0.93)
        plot = plotfig.add_subplot(111)
        plot.set_title("Wykres zależności szybkości spalania "
            "SPR od ciśnienia w komorze spalania")
        plot.set_xlabel("ln(p)")
        plot.set_ylabel("ln(u)")
        plot.grid()

        cords = self.get_plot_cords(output)
        points = plot.scatter(*cords, color="red")
        for i in range(len(cords[0])):
            plot.annotate(i+1, (cords[0][i], cords[1][i]))

        A_log = math.log(output.A)
        n = output.n
        f = lambda x: A_log + n*x
        xs = cords[0][0], cords[0][-1]
        ys = f(xs[0]), f(xs[1])
        line = plot.axline((xs[0], ys[0]), (xs[1], ys[1]), ls="--")
        plot.legend((points, line), ("Pomiar", "Aproksymacja"))
        return plotfig
