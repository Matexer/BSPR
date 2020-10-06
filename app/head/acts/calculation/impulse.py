from typing import Tuple
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
            f"WYNIKI OBLICZEŃ DLA PALIWA {self.fuel_name}")
        data = self.get_table_data(output)
        table = frame.create_table(frame.interior, data)

        title.pack(fill="both")
        table.pack(pady=20)

    @staticmethod
    def get_table_data(output: ImpulseOutput) -> Tuple[tuple, ...]:
        headings = ("Nr. pomiaru", "Impuls\ncałkowity", "Impuls\njednostkowy", "a")
        data = [(i, item.total_impulse, item.unit_impulse) 
                for i, item in enumerate(output, start=1)]
        return tuple((headings, *data))
