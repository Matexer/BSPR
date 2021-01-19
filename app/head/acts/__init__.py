from .add_fuel import AddFuelAct
from .list import FuelsListAct, SurveysListAct
from .edit_fuel import EditFuelAct
from .add_survey import AddSurveyAct
from .edit_survey import EditSurveyAct
from .config_calculation import ConfigImpulseAct
from .config_calculation import ConfigAnAct
from .config_calculation import ConfigEngineParaAct

from ..database import Database as db


def test_db():
    db.test_db()

def load_acts(top):
    acts = (AddFuelAct(top),
            FuelsListAct(top),
            EditFuelAct(top),
            AddSurveyAct(top),
            SurveysListAct(top),
            EditSurveyAct(top), # 5
            ConfigImpulseAct(top),
            ConfigAnAct(top),
            ConfigEngineParaAct(top)
            )
    return acts
