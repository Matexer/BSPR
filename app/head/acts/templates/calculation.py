from tkinter import filedialog as fd
import csv
from typing import Tuple, Any, Union, Literal
from ....core import Impulse, ImpulseOutput, Data, Config
from ....gui.TopWindow import TopWindow


class CalculationActTemplate:
    FRAME_NUMBER = 12


    def __init__(self, top: TopWindow, 
        f_name: str, data: Data, config: Config):
        self.frame = top.frames[self.FRAME_NUMBER]
        self.clean_frame()

    def clean_frame(self):
        for child in self.frame.interior.winfo_children():
            child.destroy()
    
    def save_csv_file(self, data: Tuple[Tuple[Union[str, float], ...], ...])\
        -> Literal[True, None]:
        filename = fd.asksaveasfilename(
            filetypes=[('CSV files','*.csv')], defaultextension="*.csv",
            initialfile="wyniki.csv")

        if not filename:
            return

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='\t',
                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in data:
                try:
                    writer.writerow(row)
                except UnicodeEncodeError:
                    row = [str(w).replace('\u22c5', "*") for w in row]
                    writer.writerow(row)

    def export_data(self, data):
        headings = [item.replace("\n", " ") for item in data[0]]
        csv_data = tuple((headings, *data[1:]))
        self.save_csv_file(csv_data)

    @staticmethod
    def get_dm_precision(dms):
        min_precision = 0
        for dm in dms:
            dm = str(dm)
            if "." in dm:
                prec = len(dm) - dm.index(".") - 1
                min_precision = max(min_precision, prec)
        return min_precision
