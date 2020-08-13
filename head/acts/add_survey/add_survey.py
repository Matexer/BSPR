from head.objects import Survey
from .add_values import AddSurveyValuesAct
from tkinter.filedialog import askopenfilename
from globals import SURVEY_TYPES, SURVEY_VALUES_SEPARATOR


class AddSurveyAct:
    def __init__(self, top):
        self.top = top
        self.frame = top.frames[3]
        self.import_frame = None

        self.fuels_data = self.get_fuels_data()
        self.add_frame_btns = self.frame.get_buttons()
        self.add_frame_cboxes = self.frame.get_comboboxes()
        self.sampling_t_entry = self.frame.init_widgets[1]

        self.set_comboboxes()
        self.set_buttons()

        val = [1, 2, 3, 4, 3, 1, 0]
        self.import_frame = self.top.frames[5]
        self.import_frame.set_raw_values(val)
        add_val_act = AddSurveyValuesAct(self.top, self.import_frame,
                                         val, 0.5)
        self.top.change_frame(5)

    def set_comboboxes(self):
        f_name = self.frame.name_cbox
        s_type = self.frame.init_widgets[0]
        fuel_names = [fuel.name for fuel in self.fuels_data]
        f_name.configure(values=fuel_names)
        s_type.configure(values=tuple(SURVEY_TYPES.keys()))

    def get_fuels_data(self):
        fuels_list_frame = self.top.frames[0]
        fuels_data = fuels_list_frame.data
        return fuels_data

    def set_buttons(self):
        import_values_btn = self.add_frame_btns[0]
        import_values_btn.configure(command=lambda: self.import_survey_values())

        fill_fuel_data_btn = self.add_frame_btns[1]
        save_btn = self.add_frame_btns[2]

    def import_survey_values(self):
        survey_type = self.get_survey_type()
        sampling_time = self.sampling_t_entry.get()
        try:
            sampling_time = float(sampling_time)
        except ValueError:
            sampling_time = False
        if survey_type and sampling_time:
            path_to_file = askopenfilename()
            if path_to_file:
                raw_survey_values = self.get_data_from_file(path_to_file, survey_type)
                if raw_survey_values:
                    self.change_frame(survey_type, raw_survey_values)
                    add_val_act = AddSurveyValuesAct(self.top, self.import_frame,
                                                     raw_survey_values, sampling_time)
            else:
                self.frame.show_message("Należy wybrać plik z wynikami pomiaru.")
        else:
            self.frame.show_message("Należy wybrać rodzaj pomiaru i\n"
                                    "podać okres próbkowania.")

    def get_survey_type(self):
        survey_type_cbox = self.add_frame_cboxes[1]
        type_name = survey_type_cbox.get()
        if type_name:
            s_type = SURVEY_TYPES[type_name]
            return s_type

    def get_data_from_file(self, path, s_type):
        try:
            file = open(path, 'r')
        except Exception:
            self.frame.show_message("Nie można otworzyć wskazanego pliku.")
        finally:
            lines = file.readlines()
            file.close()
            if s_type == "pressthru":
                data = [[], []]
                for line in lines:
                    line = (line.strip())
                    line = line.split(SURVEY_VALUES_SEPARATOR)
                    if len(line) == 2:
                        data[0].append(line[0])
                        data[1].append(line[1])
                    else:
                        self.frame.show_message("Nie można odczytać pomiaru ciśnienia"
                                                " i ciągu. Sprawdź plik.")
                        return False
            else:
                data = []
                for line in lines:
                    line = (line.strip())
                    data.append(line)
            data = self.validate_data(data)
            return data

    def validate_data(self, data):
        error_message = "Nie można importować danych ponieważ nie wszystkie\n" \
                        "wartości to liczby. Sprawdź plik pomiaru."
        if isinstance(data[0], (tuple, list)):
            valid_data = []
            for container in data:
                try:
                    container = [float(value) for value in container]
                except ValueError:
                    self.frame.show_message(error_message)
                    return False
                valid_data.append(container)
        else:
            try:
                valid_data = [float(value) for value in data]
            except ValueError:
                self.frame.show_message(error_message)
                return False

        return valid_data

    def change_frame(self, survey_type, raw_values):
        if survey_type == "press":
            self.top.change_frame(5)
            self.import_frame = self.top.frames[5]
        elif survey_type == "thrust":
            self.top.change_frame(6)
            self.import_frame = self.top.frames[6]
        elif survey_type == "pressthru":
            self.top.change_frame(7)
            self.import_frame = self.top.frames[7]
        self.import_frame.set_raw_values(raw_values)
