import tkinter as tk
from .add_fuel import AddFuelFrameTemplate
from gui.elements import TitleLabel
from gui.configure import TL_FG2, TL_BG


class EditFuelFrame(AddFuelFrameTemplate):
    def __init__(self, top):
        super().__init__(top)
        cancel_btn = self.buttons[2]
        cancel_btn.configure(text="POWRÓT")

    def create_head_section(self):
        title_cont, name_part = self.create_title(f_name='')
        title_cont.pack(side="top", fill="x")
        self.name_entry = tk.Entry(self)
        self.fuel_name = name_part

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
        comment = values[7].rstrip()
        values = values[1:7]
        self.fuel_name.configure(text=f_name)
        self.clear_entries()
        self.name_entry.insert(0, f_name)
        fields = self.inputs_table.inputs
        for field, value in zip(fields, values):
            field.entry.insert(0, value)

        self.comment.insert('end', comment)
