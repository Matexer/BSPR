import tkinter as tk
from gui.frames import gui_frames


class TopWindow(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.configure(background="red")
        self.pack(fill="both", expand=1)
        self.frames = self.set_frames()
        self.frames[0].pack(side="left", fill="y")

    def set_frames(self):
        frames = []
        for frame in gui_frames:
            frames.append(frame(self))
        return frames
