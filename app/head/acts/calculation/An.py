from typing import Tuple, List
import math
import tkinter as tk
from ..templates import CalculationActTemplate
from ....core import An, AnOutput
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
        frame: ResultsFrame, output: AnOutput):
        title = frame.create_title(frame.interior, 
            "WYNIKI OBLICZEŃ WSPÓŁCZYNNIKÓW A i n PRAWA "
            f"SZYBKOŚCI SPALANIA DLA PALIWA {self.fuel_name}")

        app_plotfig = self.draw_approx_plot(frame, output)

        An_subtitle = frame.create_subtitle(frame.interior, "Wartości charakterystyk")
        final_output = tk.Label(frame.interior, text=f"A = {output.A:.3e} m/(s⋅Pa^n)\
            n = {output.n:.3g}", font=("bold", 20))

        table_subtitle = frame.create_subtitle(frame.interior, "Tabela wyników")
        data = self.get_table_data(output)
        table = frame.create_table(frame.interior, data)

        export_btn = frame.create_export_btn(frame.interior)

        wp_subtitle = frame.create_subtitle(frame.interior, "Wykresy pomiarów")
        wp_plotfig = self.draw_work_p_plots(frame, output)

        title.pack(fill="both")
        app_plotfig.pack(expand=1, fill="both")
        An_subtitle.pack(fill="both", pady=5)
        final_output.pack(pady=10)
        table_subtitle.pack(fill="both", pady=5)
        table.pack()
        export_btn.pack(pady=5)
        wp_subtitle.pack(fill="both", pady=5)
        wp_plotfig.pack(expand=1, fill="both")

        data.append('')
        data.append(("A [m/(s⋅Pa^n)]", output.A, "n", output.n), )
        export_btn.configure(command=lambda: self.export_data(data))

    def get_table_data(self, output: AnOutput)\
        -> List[tuple]:
        if self.config.calculation_method == 0: #average
            headings = ("Nr\npomiaru", "p śr.\n[MPa]", "u śr.\n[mm/s]","t0\n[ms]", "tk\n[ms]", 
                "Ipk\n[MPa⋅s]", "Śr. kryt.\ndyszy [mm]", "Min. śr. kryt.\ndyszy [mm]")
            data = [(i, round(item.p/1000_000, 3), round(item.u*1000, 1), *item.times[:-1],
                    round(item.Ipk/1000_000, 3), item.jet_d, round(item.d_min, 1))
                    for i, item in enumerate(output.surveys_details, start=1)]
            return list((headings, *data))
        
        headings = ("Nr.\npomiaru", "p chw.\n[MPa]", "u chw.\n[mm/s]","t0\n[ms]", "tk\n[ms]", 
            "Ipk\n[MPa⋅s]", "Śr. kryt.\ndyszy [mm]", "Min. śr. kryt.\ndyszy [mm]", "t chwil.\n[ms]")
        data = [(i, round(item.p/1000_000, 3), round(item.u*1000, 1), *item.times[:-1],
                round(item.Ipk/1000_000, 3), item.jet_d, round(item.d_min, 1),
                round(item.point_time, 1))
                for i, item in enumerate(output.surveys_details, start=1)]
        return list((headings, *data))

    @staticmethod
    def get_plot_cords(output: AnOutput)\
        -> Tuple[tuple, tuple]:
        xs = tuple(math.log(survey.p) for survey in output.surveys_details)
        ys = tuple(math.log(survey.u) for survey in output.surveys_details)
        return xs, ys

    def draw_approx_plot(self, frame, output):
        plotfig = frame.create_plot(frame.interior)
        plotfig.figure.subplots_adjust(left=0.095, top=0.883)
        plot = plotfig.add_subplot(111)
        plot.set_title("Wykres zależności szybkości spalania SPR od ciśnienia w komorze spalania\n"
         "we współrzędnych logarytmicznych")
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

    def draw_work_p_plots(self, frame, output):
        subplots_rows = math.ceil(len(output.surveys_details) / 2)
        figsize = (1, subplots_rows * 5)
        plotfig = frame.create_plot(frame.interior, figsize=figsize)
        top = 0.971 if subplots_rows > 1 else 0.95
        plotfig.figure.subplots_adjust(left=0.071, bottom=0.048,
            right=0.998, top=top, wspace=0.145, hspace=0.200)

        for i, d in enumerate(zip(output.surveys_details, output.work_pressures), start=1):
            wp = d[1]
            d = d[0]
            size = subplots_rows, 2, i
            self.draw_subplot(plotfig, size, d.smp_time, d.press_values, 
                wp, d.times[0], d.times[1], d.jet_d, d.point_time)

        return plotfig

    @staticmethod
    def draw_subplot(plotfig, size, smp_time, press_values, wp, t0, tk, jet_d, t=None):
        plt = plotfig.add_subplot(size)
        time = tuple((smp_time * i for i in range(len(press_values))))
        plt.plot(time, press_values)
        plt.axhline(wp, color="red")
        plt.axvline(t0, color="green", linestyle="--")
        plt.axvline(tk, color="pink", linestyle="--")
        plt.axis(xmin=t0 - 10, ymin=0,
            ymax=max(wp, *press_values) * 1.05, xmax=tk * 1.1)
        plt.set_title(f"Pomiar nr {size[-1]}, ŚKD = {jet_d} mm")
        plt.set_xlabel("Czas [ms]")
        plt.set_ylabel("Ciśnienie [MPa]")
        legend = ["ciśnienie", f"ciśnienie robocze\n{str(round(wp,2)).replace('.', ',')} MPa",
        f"t0 = {int(round(t0, 0))} ms", f"tk = {int(round(tk, 0))} ms"]
        if t != None:
            plt.axvline(t, color="orange", linestyle="--")
            legend.append(f"t = {int(round(t, 0))} ms")
        plt.legend(legend)
