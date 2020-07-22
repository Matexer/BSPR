import tkinter as tk
from gui.elements import *
from gui.configure import TL_BG


class AddFuelFrame(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)

        title = self.create_title()
        name_container, name_entry = self.create_name_container()
        inputs_subtitle = self.create_inputs_subtitle()
        inputs_container, table = self.create_inputs_container()
        comment_subtitle = self.create_comment_subtitle()
        comment_container, comment = self.create_comment_container()
        btns_container, buttons = self.create_buttons_container()

        title.pack(side="top", fill="x")
        name_container.pack(side="top", anchor="w", padx=5, pady=20)
        inputs_subtitle.pack(side="top", fill="x")
        inputs_container.pack(side="top", anchor="w", padx=5)
        comment_subtitle.pack(side="top", fill="x")
        comment_container.pack(side="top", anchor="w", padx=5)
        btns_container.pack(side="bottom", fill="x")

    def create_title(self):
        title = TitleLabel(self)
        title.configure(text="DODAWANIE NOWEGO PALIWA")
        return title

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

    def create_inputs_subtitle(self):
        subtitle = SubtitleLabel(self)
        subtitle.configure(text="DANE OD PRODUCENTA")
        return subtitle

    def create_inputs_container(self):
        inputs_container = tk.Frame(self)
        variables = (("Średnica zewnętrzna\nładunku paliwa [mm]",
                      "Średnica wewnętrzna\nładunku paliwa [mm]",
                      "Długość ładunku\npaliwa [mm]",
                      "Masa paliwa [g]"),
                     ("Siła paliwa [MJ/kg]",
                      "Wykładnik adiabaty gazowych\nproduktów spalania"))
        table = InputTable(inputs_container, variables)
        table.pack()
        return inputs_container, table

    def create_comment_subtitle(self):
        subtitle = SubtitleLabel(self)
        subtitle.configure(text="KOMENTARZ")
        return subtitle

    def create_comment_container(self):
        comment_container = tk.Frame(self)
        comment = tk.Text(comment_container)
        comment.configure(width=100,
                          height=8)
        comment.pack(pady=5)
        return comment_container, comment

    def create_buttons_container(self):
        btns_container = tk.Frame(self)
        btns_container.configure(bg=TL_BG)
        save_btn = SaveButton(btns_container)
        clear_btn = ClearButton(btns_container)
        cancel_btn = CancelButton(btns_container)
        config = {"padx": 5, "pady": 5, "ipadx": 2, "ipady": 2}
        save_btn.pack(side="right", **config)
        cancel_btn.pack(side="left", **config)
        clear_btn.pack(side="left", **config)
        return btns_container, (save_btn, clear_btn, cancel_btn)


