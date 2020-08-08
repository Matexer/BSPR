from .add_fuel import AddFuelAct
from .fuels_list import FuelsListAct
from .edit_fuel import EditFuelAct


def load_acts(top):
    acts = [AddFuelAct(top),
            FuelsListAct(top),
            EditFuelAct(top)
            ]
    return acts
