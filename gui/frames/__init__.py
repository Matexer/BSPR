from gui.frames.left_menu import LeftMenuFrame
from gui.frames.top_menu import TopMenuFrame
from gui.frames.fuels_list import FuelsListFrame
from gui.frames.add_fuel import AddFuelFrame
from gui.frames.surveys_list import SurveysListFrame
from gui.frames.add_survey import AddSurveyFrame,\
                                  AddSurveyPressureValuesFrame,\
                                  AddSurveyDoubleValuesFrame,\
                                  AddSurveyThrustValuesFrame
from gui.frames.edit_fuel import EditFuelFrame


def load_frames(top):
    frames = [FuelsListFrame(top),
              AddFuelFrame(top),
              SurveysListFrame(top),
              AddSurveyFrame(top),
              EditFuelFrame(top),
              AddSurveyPressureValuesFrame(top),    #5
              AddSurveyThrustValuesFrame(top),
              AddSurveyDoubleValuesFrame(top)
              ]
    return frames
