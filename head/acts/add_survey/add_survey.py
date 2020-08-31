from tkinter.filedialog import askopenfilename
from .add_values import AddSurveyValuesAct
from head.objects import Survey
from globals import SURVEY_TYPES, SURVEY_VALUES_SEPARATOR, PRESS,\
                    THRUST
from gui.configure import IMP_VALUES_BTN_COLOR_1
import head.database as db


class AddSurveyAct:
    def __init__(self, top):
        self.top = top
        self.set_frame(top)

        self.import_frame = None
        self.survey = Survey()
        self.fuels_data = self.get_fuels_data()
        self.add_frame_cboxes = self.frame.get_comboboxes()
        self.sampling_t_entry = self.frame.init_widgets[1]

        self.set_comboboxes()
        self.set_buttons()

    def set_frame(self, top):
        self.frame = top.frames[3]

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
        import_values_btn, fill_fuel_data_btn,\
        save_btn, clear_btn, cancel_btn, modify_val_btn = self.frame.get_buttons()

        import_values_btn.configure(
            command=lambda: self.import_survey_values())
        modify_val_btn.configure(
            command=lambda: self.change_frame(self.survey.type))
        fill_fuel_data_btn.configure(
            command=lambda: self.fill_fuel_data())

        save_btn.configure(command=lambda: self.save_survey())
        clear_btn.configure(command=lambda: self.clear())
        cancel_btn.configure(command=lambda: self.cancel())

    def save_survey(self):
        values = self.frame.get_inserted_values()
        report, values = self.validate_values(values)
        if not report:
            if not self.survey.values:
                self.frame.show_message("Wymagany jest import pliku z wynikami pomiarów")
            else:
                self.add_survey_to_database(values)
                self.end_adding_survey()
                self.frame.show_message("Pomyślnie dodano nowy pomiar", "green")
        else:
            self.frame.point_entries(report)

    def clear(self):
        self.end_adding_survey()
        self.frame.clear_entries()

    def cancel(self):
        self.clear()
        self.top.change_frame(2)

    def end_adding_survey(self):
        self.survey.__init__()
        self.frame.hide_message()
        self.change_buttons()
        self.top.frames[2].refresh_list(event=1)
        tree = self.top.frames[2].tree_list.tree
        try:
            tree.selection_set(tree.get_children()[-1])
        except IndexError:
            pass

    def change_buttons(self):
        self.frame.init_widgets[2].config(
            text="Importuj plik", background=IMP_VALUES_BTN_COLOR_1)
        self.frame.init_widgets[3].pack_forget()

    def add_survey_to_database(self, values):
        f_name = values[0]
        self.survey.update(
            [self.survey.type, self.survey.sampling_time] + values[1:])
        db.save_survey(f_name, self.survey)

    def fill_fuel_data(self):
        def fill_fuel_table(values):
            table = self.frame.fuel_table
            for row, value in zip(table.inputs, values):
                row.entry.delete("0", "end")
                row.entry.insert("0", value)

        def get_fuel_data(name):
            fuels_data = self.get_fuels_data()
            for fuel in fuels_data:
                if fuel.name == name:
                    return list(fuel.export().values())[1:5]

        name = self.frame.name_cbox.get()
        if name:
            fill_fuel_table(get_fuel_data(name))
        else:
            self.frame.show_message("Aby automatycznie wypełnić informacje o paliwie,\n"
                                    "należy najpierw wybrać dla jakiego paliwa jest pomiar.")

    @staticmethod
    def validate_values(values):
        report = [1] * len(values)
        name = values[0]
        report[-1] = 0

        if name != "":
            report[0] = 0
        else:
            report[0] = "Wymagana jest nazwa paliwa."

        for i, val in enumerate(values[1:-1]):
            try:
                values[i+1] = float(val)
            except ValueError:
                report[i+1] = "Wartość musi być liczbą."

        for num, val in enumerate(values[1:-1]):
            if isinstance(val, float):
                if val > 0:
                    report[num+1] = 0
                else:
                    report[num+1] = "Wartość musi być dodatnia."

        outer_d = values[6]
        inner_d = values[7]
        if isinstance(inner_d, float):
            if inner_d == 0:
                report[7] = 0

        if isinstance(outer_d, (float, int)) and isinstance(inner_d, (int, float)):
            if inner_d >= outer_d:
                report[7] = "Średnica wewnętrzna musi być mniejsza od zewnętrznej."

        sum_up = set(report)
        if sum_up == {0}:
            report = False

        return report, values

    def import_survey_values(self):
        self.survey.__init__()
        survey_type = self.get_survey_type()
        sampling_time = self.sampling_t_entry.get()

        try:
            sampling_time = float(sampling_time)
        except ValueError:
            self.frame.show_message("Czas próbkowania musi być liczbą.")
            return

        if survey_type:
            path_to_file = askopenfilename()
        else:
            self.frame.show_message("Należy wybrać rodzaj pomiaru.")
            return

        if path_to_file:
            raw_survey_values = self.get_data_from_file(path_to_file)
        else:
            self.frame.show_message("Należy wybrać plik z wynikami pomiaru.")
            return

        if raw_survey_values:
            self.survey.update({"type": survey_type,
                                "sampling_time": sampling_time,
                                "raw_values": raw_survey_values[:],
                                "values": raw_survey_values[:],
                                "multipliers": [1 for _ in raw_survey_values]})
            self.start_adding_act()

    def start_adding_act(self):
        self.change_frame(self.survey.type)
        AddSurveyValuesAct(self.top, self.import_frame, self.survey)

    def get_survey_type(self):
        survey_type_cbox = self.add_frame_cboxes[1]
        type_name = survey_type_cbox.get()
        if type_name:
            s_type = SURVEY_TYPES[type_name]
            return s_type

    def get_data_from_file(self, path):
        try:
            file = open(path, 'r')
        except Exception:
            self.frame.show_message("Nie można otworzyć wskazanego pliku.")
        finally:
            lines = file.readlines()
            file.close()
            line = lines[0].strip().split(SURVEY_VALUES_SEPARATOR)
            data = []
            for _ in range(len(line)):
                data.append([])
            for line in lines:
                line = line.strip().split(SURVEY_VALUES_SEPARATOR)
                for num, column in enumerate(line):
                    data[num].append(column)
            data = self.validate_imported_data(data)
            return data

    def validate_imported_data(self, data):
        error_message = "Nie można importować danych ponieważ nie wszystkie\n" \
                        "wartości to liczby. Sprawdź plik pomiaru."
        valid_data = []
        for column in data:
            try:
                valid_column = [float(value) for value in column]
            except ValueError:
                self.frame.show_message(error_message)
                return False
            valid_data.append(valid_column)

        return valid_data

    def change_frame(self, survey_type):
        if survey_type == PRESS:
            frame_num = 5
        elif survey_type == THRUST:
            frame_num = 6
        else:
            frame_num = 7
        self.top.change_frame(frame_num)
        self.import_frame = self.top.frames[frame_num]
