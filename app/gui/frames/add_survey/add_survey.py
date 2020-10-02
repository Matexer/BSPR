import tkinter as tk
import tkinter.ttk as ttk
from gui.frames.templates import FrameTemplate
from gui.elements import Button, SubtitleLabel
from gui.configure import STL_BG, IMP_VALUES_BTN_COLOR_1,\
    FILL_FUEL_BTN_COLOR, CHANGE_IMP_VALUES_BTN_COLOR


class AddSurveyFrameTemplate(FrameTemplate):
    def __init__(self, top):
        super().__init__(top)
        self.create_head_section()
        self.create_body_section()

    def get_buttons(self):
        import_values_btn = self.init_widgets[2]
        modify_values_btn = self.init_widgets[3]
        fill_fuel_data_btn = self.fill_btn
        save_btn, clear_btn, cancel_btn = self.buttons
        return import_values_btn, fill_fuel_data_btn,\
               save_btn, clear_btn, cancel_btn, modify_values_btn

    def get_comboboxes(self):
        name_cbox = self.name_cbox
        survey_type_cbox = self.init_widgets[0]
        return name_cbox, survey_type_cbox

    def create_head_section(self):
        self.title = self.create_title(self, "DODAWANIE NOWEGO POMIARU")
        name_container, self.name_cbox = self.create_name_container()
        init_container, self.init_widgets = self.create_init_survey_container()

        self.title.pack(side="top", fill="x")
        name_container.pack(side="top", anchor="w", padx=5, pady=10)
        init_container.pack(side="top", anchor="w", fill="x", padx=5)

    def create_body_section(self):
        survey_subtitle = self.create_subtitle(self, "DANE POMIARU")
        variables = (("Średnica krytyczna\ndyszy [mm]",),

                     ("Średnica komory\nspalania [mm]",
                      "Długość komory\nspalania [mm]"),

                     ("Współczynnik strat\nwydatku",
                      "Współczynnik strat\ncieplnych"))
        survey_container, self.survey_table = self.create_inputs_container(self, variables)
        fuel_subtitle, self.fill_btn = self.create_fuel_subtitle("DANE PALIWA")
        variables = (("Średnica zewnętrzna\nładunku paliwa [mm]",
                      "Średnica wewnętrzna\nładunku paliwa [mm]"),

                     ("Długość ładunku\npaliwa [mm]",
                      "Masa paliwa [g]"))
        fuel_container, self.fuel_table = self.create_inputs_container(self, variables)
        comment_subtitle = self.create_subtitle(self, "KOMENTARZ")
        comment_container, self.comment = self.create_comment_container(self, 100, 6)
        btns_container, self.buttons = self.create_down_nav_container(self)

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

        import_btn = Button(init_survey_container)
        import_btn.configure(text="Importuj plik",
                             background=IMP_VALUES_BTN_COLOR_1)
        import_btn.pack(side="left", padx=10, pady=5)

        modify_btn = Button(init_survey_container)
        modify_btn.configure(text="Modyfikuj pomiar",
                             background=CHANGE_IMP_VALUES_BTN_COLOR)
        return init_survey_container, (cbox, entry, import_btn, modify_btn)

    def create_fuel_subtitle(self, text):
        container = tk.Frame(self)
        container.configure(background=STL_BG)
        subtitle = SubtitleLabel(container)
        subtitle.configure(text=text)
        btn = Button(container)
        btn.configure(text="Wypełnij",
                      background=FILL_FUEL_BTN_COLOR,
                      borderwidth=0)
        subtitle.pack(side="left")
        btn.pack(side="left", padx=5)
        return container, btn

    def get_inserted_values(self):
        fuel_name = [self.name_cbox.get()]
        survey_inputs = self.survey_table.get_inserted_values()
        fuel_inputs = self.fuel_table.get_inserted_values()
        comment = [self.comment.get('1.0', 'end')]
        return fuel_name + survey_inputs + fuel_inputs + comment

    def point_entries(self, reports):
        name_report = reports[0]
        survey_table_reports = reports[1:6]
        fuel_table_reports = reports[6:10]
        if name_report == 0:
            self.name_cbox.configure(background="white")
        else:
            self.name_cbox.configure(background="red")
        self.survey_table.point_entries(survey_table_reports)
        self.fuel_table.point_entries(fuel_table_reports)
        for report in reports:
            if report:
                self.show_message(report)
                return

    def clean(self):
        self.name_cbox.set('')
        self.init_widgets[0].set('')
        self.init_widgets[1].delete('0', "end")
        self.name_cbox.configure(background="white")
        self.survey_table.clean()
        self.fuel_table.clean()
        self.comment.delete("1.0", 'end')
        self.hide_message(num=-1)
