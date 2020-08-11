from .add_fuel import AddFuelAct
from .fuels_list import FuelsListAct
from .edit_fuel import EditFuelAct
from .add_survey import AddSurveyAct


def load_acts(top):
    acts = [AddFuelAct(top),
            FuelsListAct(top),
            EditFuelAct(top),
            AddSurveyAct(top)
            ]
    return acts
