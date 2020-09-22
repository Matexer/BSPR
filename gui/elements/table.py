import tkinter as tk
from itertools import cycle
from typing import Tuple, List, Union


class Element(tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(font=14)


class Heading(Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(font="bold")


Fields = List[Tuple[Element]]
Listing = Union[List, Tuple]


class TableFrame(tk.Frame):
    HEADING_COLORS = ("SkyBlue3", "LightCyan4")
    ROW_COLORS = (("LightSkyBlue3", "SlateGray3"),
                  ("LightSkyBlue2", "SlateGray2")
                  )
    HEADINGS = True

    def __init__(self, master, data, *args, **kwargs):
        self.__update_vars(kwargs)
        super().__init__(master, *args, **kwargs)
        self.fields: Fields = []
        table_width = len(data[0])
        self.heading_colors = self.__get_headings_colors(table_width)
        self.row_colors = self.__get_row_colors(table_width)
        self.__create_table(data)

    def __update_vars(self, kwargs: dict):
        variables = "heading_colors", "row_colors", "headings"
        for key in variables:
            if key in kwargs:
                self.__setattr__(key.upper(), kwargs.pop(key))

    def __get_headings_colors(self, length: int)\
            -> Tuple[str]:
        heading_colors = cycle(self.HEADING_COLORS)
        return tuple(next(heading_colors)
                     for _ in range(length))

    def __get_row_colors(self, length: int):
        rows_colors = (cycle(row) for row in self.ROW_COLORS)
        rows = []
        for row_colors in rows_colors:
            rows.append(tuple(next(row_colors) for _ in range(length)))
        return rows

    def __create_table(self, data: List):
        start = 0
        if self.HEADINGS:
            self.fields.append(self.__create_headings(data[0]))
            start = 1
        for row, row_color_num in zip(
                data[start:], cycle(i for i in range(len(self.ROW_COLORS)))):
            self.fields.append(self.__create_row(row, self.row_colors[row_color_num]))
        self.__grid_table(self.fields)

    def __create_headings(self, headings: Listing)\
            -> Tuple[Heading]:
        return tuple(Heading(self, text=cont, bg=col)
                     for cont, col in zip(headings, self.heading_colors))

    def __create_row(self, row_data: Listing, colors: Tuple[str])\
            -> Tuple[Element]:
        return tuple(Element(self, text=cont, bg=col)
                     for cont, col in zip(row_data, colors))

    @staticmethod
    def __grid_table(table: Fields):
        for r_num, row in enumerate(table):
            for c_num, element in enumerate(row):
                element.grid(row=r_num, column=c_num, sticky='WENS')


if __name__ == "__main__":
    import tkinter as tk

    root = tk.Tk()
    table_data = (("Head 1", "Head 2", "Head 3", "Head 4"),
                    (1, 2, 3, 5),
                    (4, "0000000000000000\n0\n0\n00000000", 6, 7),
                    (7, 8, 9, 9),
                    (7, 8, 9, 9),
                    (7, 8, 9, 9)
                    )
    table = TableFrame(root, table_data)
    table.pack()
    root.mainloop()
