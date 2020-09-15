from gui.TopWindow import TopWindow


class ConfigCalculationActTemplate:
    INPUT_VARIABLES = (("Var 1", "Var 2"),
                       ("Var 3", "Var 4"))

    CBOX_VARIABLES = (({"Set 1": ("op. 1", "op. 2", "op. 3")},
                       {"Set 2": ("op. 1", "op. 2", "op. 3")}),

                      ({"Set 3": ("op. 1", "op. 2", "op. 3")},
                       {"Set 4": ("op. 1", "op. 2", "op. 3")}))

    LIST_COLUMNS = ("ŚKD [mm]", )

    def __init__(self, top: TopWindow):
        self.top = top
