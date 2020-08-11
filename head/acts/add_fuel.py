from globals import FORBIDDEN_NAME_SIGNS
import head.database as db
from head.objects import Fuel


class AddFuelAct:
    def __init__(self, top):
        self.frame = top.frames[1]
        self.set_button(self.frame)
        self.top = top

    def set_button(self, frame):
        save_btn = frame.buttons[0]
        save_btn.configure(command=lambda: self.save_fuel())

    def save_fuel(self):
        values = self.frame.get_inserted_values()
        report, values = self.validate_values(values)
        if not report:
            self.add_fuel_to_database(values)
        else:
            self.frame.point_entries(report)

    def validate_values(self, values):
        report = [1] * len(values)
        name = values[0]
        # outer_d = values[1]
        # inner_d = values[2]
        # length = values[3]
        # mass = values[4]
        # strength = values[5]
        # k = values[6]
        # comment = values[7]
        report[7] = 0

        if name != "":
            if not set(name).intersection(FORBIDDEN_NAME_SIGNS):
                if not self.is_name_free(name):
                    report[0] = "Ta nazwa jest już zajęta."
                else:
                    report[0] = 0
            else:
                report[0] = "Niedozwolone znaki %s w nazwie paliwa." % FORBIDDEN_NAME_SIGNS

        for i, val in enumerate(values[1:7]):
            try:
                values[i+1] = float(val)
            except ValueError:
                report[i+1] = "Wartość musi być liczbą."

        for num, val in enumerate(values[1:7]):
            if isinstance(val, float):
                if val > 0:
                    report[num+1] = 0
                else:
                    report[num+1] = "Wartość musi być dodatnia."

        outer_d = values[1]
        inner_d = values[2]
        if isinstance(inner_d, float):
            if inner_d == 0:
                report[2] = 0

        if isinstance(outer_d, (float, int)) and isinstance(inner_d, (int, float)):
            if inner_d > outer_d:
                report[2] = "Średnica wewnętrzna nie może być większa od zewnętrznej."

        sum_up = set(report)
        if sum_up == {0}:
            report = False

        return report, values

    @staticmethod
    def is_name_free(name):
        used_names = db.get_fuels_list()
        if name in used_names:
            return False
        else:
            return True

    def add_fuel_to_database(self, values):
        new_fuel = Fuel()
        new_fuel.update(values)
        try:
            db.save_fuel(new_fuel)
        except Exception:
            self.frame.show_message("Nie udało się zapisać paliwa.")
        finally:
            list_frame = self.top.frames[0]
            list_frame.reload_list()
            f_id = list_frame.get_id_by_name(new_fuel.name)
            list_frame.tree_list.tree.selection_set(f_id)
            self.frame.show_message("Zapisano pomyślnie.", "green")
