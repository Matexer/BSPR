import tkinter as tk
from gui.configure import *


class Button(tk.Button):
    def __init__(self, top):
        tk.Button.__init__(self, top)


class AddButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(background="green",
                       font="bold",
                       cursor="hand2",
                       text="Dodaj")


class DeleteButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(background="red",
                       font="bold",
                       cursor="hand2",
                       text="Usuń")


class EditButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(background="yellow",
                       font="bold",
                       cursor="hand2",
                       text="Edytuj")

