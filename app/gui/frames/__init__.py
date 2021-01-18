from .left_menu import LeftMenuFrame
from .top_menu import TopMenuFrame
from .fuels_list import FuelsListFrame
from .add_fuel import AddFuelFrame
from .surveys_list import SurveysListFrame
from .add_survey import AddSurveyFrame,\
                                  AddSurveyPressureValuesFrame,\
                                  AddSurveyDoubleValuesFrame,\
                                  AddSurveyThrustValuesFrame
from .edit_fuel import EditFuelFrame
from .edit_survey import EditSurveyFrame
from .config_impulse import ConfigImpulseFrame
from .config_An import ConfigAnFrame
from .config_enginepara import ConfigEngineParametersFrame
from .results_frame import ResultsFrame


def load_frames(top):
    frames = (FuelsListFrame(top),                  #0
              AddFuelFrame(top),                    #1
              SurveysListFrame(top),                #2
              AddSurveyFrame(top),                  #3
              EditFuelFrame(top),                   #4
              AddSurveyPressureValuesFrame(top),    #5
              AddSurveyThrustValuesFrame(top),
              AddSurveyDoubleValuesFrame(top),
              EditSurveyFrame(top),
              ConfigImpulseFrame(top),
              ConfigAnFrame(top),                   #10
              ConfigEngineParametersFrame(top),
              ResultsFrame(top)
              )
    return frames
