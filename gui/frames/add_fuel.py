import tkinter as tk
from .templates import FrameTemplate


class AddFuelFrameTemplate(FrameTemplate):
    def __init__(self, top):
        super().__init__(top)
        self.create_head_section()
        self.create_body_section()

    def create_head_section(self):
        title = self.create_title(self, "DODAWANIE NOWEGO PALIWA")
        name_container, self.name_entry = self.create_name_container()

        title.pack(side="top", fill="x")
        name_container.pack(side="top", anchor="w", padx=5, pady=20)

    def create_body_section(self):
        inputs_subtitle = self.create_subtitle(self, "DANE OD PRODUCENTA")

        variables = (("Średnica zewnętrzna\nładunku paliwa [mm]",
                      "Średnica wewnętrzna\nładunku paliwa [mm]"),
                      
                      ("Długość ładunku\npaliwa [mm]",
                      "Masa paliwa [g]"),
                      
                      ("Siła paliwa [MJ/kg]",
                      "Wykładnik adiabaty gazowych\nproduktów spalania"))

        inputs_container, self.inputs_table = self.create_inputs_container(self, variables)
        comment_subtitle = self.create_subtitle(self, "KOMENTARZ")
        comment_container, self.comment = self.create_comment_container(self)
        btns_container, self.buttons = self.create_down_nav_container()
        self.set_buttons(self.buttons)

        inputs_subtitle.pack(side="top", fill="x")
        inputs_container.pack(side="top", anchor="w", padx=5)
        comment_subtitle.pack(side="top", fill="x")
        comment_container.pack(side="top", anchor="w", padx=5)
        btns_container.pack(side="bottom", fill="x")

    def set_buttons(self, btns):
        clear_btn = btns[1]
        cancel_btn = btns[2]
        clear_btn.configure(command=lambda: self.clear_entries())
        cancel_btn.configure(command=lambda: self.top.change_frame(0))

    def create_name_container(self):
        name_container = tk.Frame(self)
        label = tk.Label(name_container)
        label.configure(text="Nazwa paliwa",
                        font="bold")
        entry = tk.Entry(name_container)
        entry.configure(width=30)
        label.grid()
        entry.grid(row=0, column=1, padx=7)
        return name_container, entry

    def get_inserted_values(self):
        name = [self.name_entry.get()]
        inputs = self.inputs_table.get_inserted_values()
        comment = [self.comment.get('1.0', 'end')]
        return name + inputs + comment

    def point_entries(self, reports):
        name_report = reports[0]
        inputs_reports = reports[1:-1]
        if name_report == 0:
            self.name_entry.configure(background="white")
        else:
            self.name_entry.configure(background="red")
        self.inputs_table.point_entries(inputs_reports)
        for report in reports:
            if report:
                self.show_message(report)
                return

    def clear_entries(self):
        self.name_entry.delete('0', 'end')
        self.name_entry.configure(background="white")
        self.inputs_table.clear_entries()
        self.comment.delete("1.0", 'end')
        self.hide_message(num=-1)

    def cancel(self):
        self.clear_entries()
        self.top.change_frame(0)
