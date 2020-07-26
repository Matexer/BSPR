import tkinter as tk


class Button(tk.Button):
    def __init__(self, top):
        tk.Button.__init__(self, top)
        self.configure(cursor="hand2",
                       font="bold",
                       highlightthickness=0
                       )

class SaveButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(text='ZAPISZ',
                       bg='green')


class ClearButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(text='WYCZYŚĆ',
                       bg='yellow')

class CancelButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(text='ANULUJ',
                       bg='red')


class AddButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(background="green",
                       text="Dodaj")


class DeleteButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(background="red",
                       text="Usuń")


class EditButton(Button):
    def __init__(self, top):
        Button.__init__(self, top)
        self.configure(background="yellow",
                       text="Edytuj")

