from gui.frames.left_menu import LeftMenuFrame
from gui.frames.top_menu import TopMenuFrame
from gui.frames.fuels_list import FuelsListFrame
from gui.frames.add_fuel import AddFuelFrameTemplate
from gui.frames.surveys_list import SurveysListFrame
from gui.frames.add_survey import AddSurveyFrameTemplate,\
                                  AddSurveyPressureValuesFrame,\
                                  AddSurveyDoubleValuesFrame,\
                                  AddSurveyThrustValuesFrame
from gui.frames.edit_fuel import EditFuelFrame
from gui.frames.edit_survey import EditSurveyFrame


def load_frames(top):
    frames = [FuelsListFrame(top),
              AddFuelFrameTemplate(top),
              SurveysListFrame(top),
              AddSurveyFrameTemplate(top),
              EditFuelFrame(top),
              AddSurveyPressureValuesFrame(top),  #5
              AddSurveyThrustValuesFrame(top),
              AddSurveyDoubleValuesFrame(top),
              EditSurveyFrame(top)
              ]
    return frames
