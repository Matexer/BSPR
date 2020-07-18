from .button import Button


class LeftMenuButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(background="green",
                       wrap=100,
                       width=13)
