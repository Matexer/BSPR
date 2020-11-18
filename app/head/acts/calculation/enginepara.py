from typing import Tuple
import tkinter as tk
from ..templates import CalculationActTemplate
from ....core import EnginePara, EngineParaOutput
from ....gui.frames import ResultsFrame


class EngineParaAct(CalculationActTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fuel_name = args[1]
        data = args[2]
        config = args[3]
        output = EnginePara(data, config).get_results()
        self.generate_report(self.frame, output)

    def generate_report(self, 
        frame: ResultsFrame, output: EngineParaOutput):
        title = frame.create_title(frame.interior, 
            "WYNIKI OBLICZEŃ WARTOŚCI WSPÓŁCZYNNIKÓW STRAT " 
            f"GAZODYNAMICZNYCH I CIEPLNYCH DLA PALIWA {self.fuel_name}")

        data = self.get_table_data(output)
        table = frame.create_table(frame.interior, data)

        export_btn = frame.create_export_btn(frame.interior)

        title.pack(fill="both")
        tk.Label(frame.interior,
            text=f"φ_1 = {output.fi1:.3g}", font=16).pack()
        tk.Label(frame.interior,
            text=f"φ_2 = {output.fi2:.3g}", font=16).pack(pady=10)
        tk.Label(frame.interior,
            text=f"λ = {output.lam:.3g}", font=16).pack(pady=10)
        table.pack(pady=20)
        export_btn.pack(pady=5)

        export_btn.configure(command=lambda: self.export_data(data))

    @staticmethod
    def get_table_data(output: EngineParaOutput) -> Tuple[tuple, ...]:
        headings = ("K0_k", "zeta_a", "Xa", "Fw","K_k\n[m^(1/2)/s]",
            "Fmin\n[mm2]", "R\n[N⋅s]", "P\n[MPa⋅s]")
        data = (f"{output.K0_k:.3g}", f"{output.zeta_a:.3g}",
            f"{output.Xa:.3g}", f"{output.Fw:.3g}",
            f"{output.K_k:.3g}", round(output.Fmin, 2),
            round(output.R, 1), round(output.P, 3))
        return headings, data
