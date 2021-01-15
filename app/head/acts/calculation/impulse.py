from typing import Tuple
from statistics import mean
from ..templates import CalculationActTemplate
from ....core import Impulse, ImpulseOutput
from ....gui.frames import ResultsFrame


class ImpulseAct(CalculationActTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fuel_name = args[1]
        data = args[2]
        config = args[3]
        output = Impulse(data, config).get_results()
        self.generate_report(self.frame, output)

    def generate_report(self, 
        frame: ResultsFrame, output: ImpulseOutput):
        title = frame.create_title(frame.interior, 
            f"WYNIKI OBLICZEŃ IMPULSU JEDNOSTKOWEGO DLA PALIWA {self.fuel_name}")
        data = self.get_table_data(output)
        table = frame.create_table(frame.interior, data)

        export_btn = frame.create_export_btn(frame.interior)

        title.pack(fill="both")
        table.pack(pady=20)
        export_btn.pack(pady=5)
        export_btn.configure(command=lambda: self.export_data(data))

    def get_table_data(self, output: ImpulseOutput) -> Tuple[tuple, ...]:
        def get_a(item):
            if item.a:
                return round(item.a, 2)
            else:
                return "-"

        dms = tuple(item.jet_d for item in output)
        min_precision = self.get_dm_precision(dms)

        headings = ("Nr\npomiaru", "Impuls jednostkowy\n[N⋅s/kg]",
            "Impuls całkowity\n[N⋅s]", "a\n[-]", "dm [mm]",
            "Dł. komory\nspalania [mm]", "Śr. komory\nspalania [mm]")

        data = [headings]

        for i, item in enumerate(output, start=1):
            row = (i, int(round(item.unit_impulse, 0)), round(item.total_impulse, 1),
                get_a(item), format(item.jet_d, f'.{min_precision}f'), item.chamber_length,
                item.chamber_d)
            data.append(row)

        return data
