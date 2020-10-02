from .left_menu import LeftMenuFrame
from .top_menu import TopMenuFrame
from .fuels_list import FuelsListFrame
from .add_fuel import AddFuelFrameTemplate
from .surveys_list import SurveysListFrame
from .add_survey import AddSurveyFrameTemplate,\
                                  AddSurveyPressureValuesFrame,\
                                  AddSurveyDoubleValuesFrame,\
                                  AddSurveyThrustValuesFrame
from .edit_fuel import EditFuelFrame
from .edit_survey import EditSurveyFrame
from .config_impulse import ConfigImpulseFrame
from .config_An import ConfigAnFrame
from .config_engine_para import ConfigEngineParametersFrame
from .templates.results_frame import ResultsFrameTemplate


def load_frames(top):
    frames = (FuelsListFrame(top),
              AddFuelFrameTemplate(top),
              SurveysListFrame(top),
              AddSurveyFrameTemplate(top),
              EditFuelFrame(top),
              AddSurveyPressureValuesFrame(top),  # 5
              AddSurveyThrustValuesFrame(top),
              AddSurveyDoubleValuesFrame(top),
              EditSurveyFrame(top),
              ConfigImpulseFrame(top),
              ConfigAnFrame(top), # 10
              ConfigEngineParametersFrame(top),
              ResultsFrameTemplate(top)
              )
    return frames
