import tkinter as tk
from .TopWindow import TopWindow
from globals import *


class GUI:
    def __init__(self):
        self.frames = []
        self.selected_frame = 0

    def start(self):
        root = tk.Tk()
        top = TopWindow(root)
        root.title(TITLE)
        root.geometry("800x400")
        root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
        root.mainloop()
        self.frames = top.frames
        return top

    def change_frame(self, id):
        self.frames[self.selected_frame].grid_forget()
        frame = self.frames[id]
        frame.grid(*frame.position)
        self.selected_frame = id


gui = GUI()


def start():
    top = gui.start()
    return top


def change_frame(id):
    gui.change_frame(id)
