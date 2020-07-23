import tkinter as tk
import tkinter.ttk as ttk
from gui.elements import Button
from gui.frames import AddFuelFrame


class AddSurveyFrame(AddFuelFrame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)

        title = self.create_title("DODAWANIE NOWEGO POMIARU")
        name_container, name_cbox = self.create_name_container()
        init_container, self.init_widgets = self.create_init_survey_container()
        inputs_subtitle = self.create_subtitle("DANE OD PRODUCENTA")
        inputs_container, table = self.create_inputs_container()
        comment_subtitle = self.create_subtitle("KOMENTARZ")
        comment_container, comment = self.create_comment_container()
        btns_container, self.buttons = self.create_buttons_container()

        title.pack(side="top", fill="x")
        name_container.pack(side="top", anchor="w", padx=5, pady=20)
        init_container.pack(side="top", anchor="w", fill="x", padx=5)
        inputs_subtitle.pack(side="top", fill="x")
        inputs_container.pack(side="top", anchor="w", padx=5)
        comment_subtitle.pack(side="top", fill="x")
        comment_container.pack(side="top", anchor="w", padx=5)
        btns_container.pack(side="bottom", fill="x")

    def create_name_container(self):
        name_container = tk.Frame(self)
        label = tk.Label(name_container)
        label.configure(text="Dla paliwa",
                        font="bold")
        cbox = ttk.Combobox(name_container)
        cbox.configure(width=30)
        label.grid()
        cbox.grid(row=0, column=1, padx=7)
        return name_container, cbox

    def create_init_survey_container(self):
        init_survey_container = tk.Frame(self)
        type_label = tk.Label(init_survey_container)
        type_label.configure(text="Rodzaj pomiaru")
        cbox = ttk.Combobox(init_survey_container)
        type_label.pack(side="left")
        cbox.pack(side="left", padx=5)

        smp_label = tk.Label(init_survey_container)
        smp_label.configure(text="Czas próbkowania [ms]")
        entry = tk.Entry(init_survey_container)
        entry.configure(width=5)
        smp_label.pack(side="left")
        entry.pack(side="left", padx=5)

        btn = Button(init_survey_container)
        btn.configure(text="Importuj plik",
                      background="orange")
        btn.pack(side="left", padx=10)
        return init_survey_container, (cbox, entry, btn)

