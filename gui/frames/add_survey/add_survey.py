import tkinter as tk
import tkinter.ttk as ttk
from gui.frames.base import BaseFrame
from gui.elements import Button, SubtitleLabel
from gui.configure import STL_BG


class AddSurveyFrame(BaseFrame):
    def __init__(self, top):
        super().__init__(top)
        self.create_head_section()
        self.create_body_section()

    def get_buttons(self):
        import_values_btn = self.init_widgets[2]
        fill_fuel_data_btn = self.fill_btn
        save_btn, clear_btn, cancel_btn = self.buttons
        return import_values_btn, fill_fuel_data_btn,\
               save_btn, clear_btn, cancel_btn

    def get_comboboxes(self):
        name_cbox = self.name_cbox
        survey_type_cbox = self.init_widgets[0]
        return name_cbox, survey_type_cbox

    def create_head_section(self):
        title = self.create_title("DODAWANIE NOWEGO POMIARU")
        name_container, self.name_cbox = self.create_name_container()
        init_container, self.init_widgets = self.create_init_survey_container()

        title.pack(side="top", fill="x")
        name_container.pack(side="top", anchor="w", padx=5, pady=10)
        init_container.pack(side="top", anchor="w", fill="x", padx=5)

    def create_body_section(self):
        survey_subtitle = self.create_subtitle("DANE POMIARU")
        variables = (("Średnica krytyczna\ndyszy [mm]",),

                     ("Średnica komory\nspalania [mm]",
                      "Długość komory\nspalania [mm]"),

                     ("Współczynnik strat\nwydatku",
                      "Współczynnik strat\ncieplnych"))
        survey_container, survey_table = self.create_inputs_container(variables)
        fuel_subtitle, self.fill_btn = self.create_fuel_subtitle("DANE PALIWA")
        variables = (("Średnica zewnętrzna\nładunku paliwa [mm]",
                      "Średnica wewnętrzna\nładunku paliwa [mm]"),

                     ("Długość ładunku\npaliwa [mm]",
                      "Masa paliwa [g]"))
        fuel_container, fuel_table = self.create_inputs_container(variables)
        comment_subtitle = self.create_subtitle("KOMENTARZ")
        comment_container, comment = self.create_comment_container(100, 6)
        btns_container, self.buttons = self.create_down_nav_container()

        survey_subtitle.pack(side="top", fill="x")
        survey_container.pack(side="top", anchor="w", padx=5)
        fuel_subtitle.pack(side="top", fill="x")
        fuel_container.pack(side="top", anchor="w", padx=5)
        comment_subtitle.pack(side="top", fill="x")
        comment_container.pack(side="top", anchor="w", padx=5)
        btns_container.pack(side="bottom", fill="x")

    def create_name_container(self):
        name_container = tk.Frame(self)
        label = tk.Label(name_container)
        label.configure(text="Dla paliwa",
                        font="bold")
        cbox = ttk.Combobox(name_container,
                            state="readonly",
                            width=30
                            )
        label.grid()
        cbox.grid(row=0, column=1, padx=7)
        return name_container, cbox

    def create_init_survey_container(self):
        init_survey_container = tk.Frame(self)
        type_label = tk.Label(init_survey_container)
        type_label.configure(text="Rodzaj pomiaru")
        cbox = ttk.Combobox(init_survey_container,
                            state="readonly")
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
        btn.pack(side="left", padx=10, pady=5)
        return init_survey_container, (cbox, entry, btn)

    def create_fuel_subtitle(self, text):
        container = tk.Frame(self)
        container.configure(background=STL_BG)
        subtitle = SubtitleLabel(container)
        subtitle.configure(text=text)
        btn = Button(container)
        btn.configure(text="Wypełnij",
                      background="azure3",
                      borderwidth=0)
        subtitle.pack(side="left")
        btn.pack(side="left", padx=5)
        return container, btn
