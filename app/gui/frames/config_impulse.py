from .templates.config_calculation_frame import ConfigCalculationFrameTemplate
from ...globals import INTEGRATION_METHODS

class ConfigImpulseFrame(ConfigCalculationFrameTemplate):
    INPUT_VARIABLES = False

    CBOX_VARIABLES = (
        {"Metoda całkowania": tuple(INTEGRATION_METHODS.keys())}
    )

    SURVEY_LIST_COLUMNS = {"ŚKD [mm]": 1}

    TITLE = "WYZNACZANIE IMPULSU JEDNOSTKOWEGO"

    @staticmethod
    def set_plot_labels(plot):
        plot.set_title("Wykres/y pomiaru ciągu od czasu")
        plot.set_xlabel("Czas [ms]")
        plot.set_ylabel("Ciąg [kN]")
    
    def create_surveys_container(self, top, columns):
        container, ch_list =\
            ConfigCalculationFrameTemplate.\
                create_surveys_container(self, top, columns)
        ch_list.plot_buttons[1].pack_forget()
        return container, ch_list
