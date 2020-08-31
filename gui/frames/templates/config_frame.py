from .frame import FrameTemplate


class ConfigFrameTemplate(FrameTemplate):
    def __init__(self, top, *args, **kwargs):
        super().__init__(top, *args, **kwargs)

    def create_config_table_container(self, top):
        pass

    def create_surveys_container(self, top, surveys):
        pass
