import tkinter as tk
from .add_fuel import AddFuelFrame
from gui.elements import TitleLabel
from gui.configure import TL_FG2, TL_BG


class EditFuelFrame(AddFuelFrame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)
        self.fuel_name = self.create_head_section()
        self.name_entry = tk.Entry(self)
        self.create_body_section()
        self.top = top

    def create_head_section(self):
        title_cont, name_part = self.create_title(f_name='')
        title_cont.pack(side="top", fill="x")
        return name_part

    def create_title(self, f_name):
        container = tk.Frame(self)
        container.configure(background=TL_BG)
        text = "EDYTOWANIE PALIWA "
        title_part = TitleLabel(container)
        title_part.configure(text=text)
        title_part.pack(side="left")

        name_part = TitleLabel(container)
        name_part.configure(text=f_name,
                            foreground=TL_FG2)
        name_part.pack(side="left")
        return container, name_part

    def set_values(self, values):
        f_name = values[0]
        comment = values[7]
        values = values[1:7]
        self.fuel_name.configure(text=f_name)
        self.clear_entries()
        self.name_entry.insert(0, f_name)
        fields = self.inputs_table.inputs
        for field, value in zip(fields, values):
            field.entry.insert(0, value)

        self.comment.insert('end', comment)
