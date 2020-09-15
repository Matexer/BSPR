from .add_fuel import AddFuelAct
from .list import FuelsListAct, SurveysListAct
from .edit_fuel import EditFuelAct
from .add_survey import AddSurveyAct
from .edit_survey import EditSurveyAct

from .templates.config_calculation import ConfigCalculationActTemplate


def load_acts(top):
    acts = [AddFuelAct(top),
            FuelsListAct(top),
            EditFuelAct(top),
            AddSurveyAct(top),
            SurveysListAct(top),
            EditSurveyAct(top),
            ConfigCalculationActTemplate(top)
            ]
    return acts
