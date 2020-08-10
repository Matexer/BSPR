from .add_fuel import AddFuelAct
from head.objects import Fuel
import head.database as db


class EditFuelAct(AddFuelAct):
    def __init__(self, top):
        self.frame = top.frames[4]
        self.set_button(self.frame)

    def validate_values(self, values):
        report, values = super().validate_values(values)
        report[0] = 0
        sum_up = set(report)
        if sum_up == {0}:
            report = False
        return report, values

    def add_fuel_to_database(self, values):
        new_fuel = Fuel()
        new_fuel.update(values)
        new_fuel.update_timedata()
        try:
            db.edit_fuel(new_fuel)
        except Exception:
            self.frame.show_message("Nie udało się zedytować paliwa.")
        finally:
            self.frame.show_message("Zedytowano pomyślnie.", "green")
