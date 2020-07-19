import tkinter as tk
from gui.frames import gui_frames
from gui.configure import *


class TopWindow(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.configure(background=TW_BG)
        self.pack(fill="both", expand=1)

        self.selected_frame = 0
        self.frames = self.__load_frames()
        self.frames[0].pack(side="left", fill="y")
        self.frames[1].pack(side="top", fill="x")

    def __load_frames(self):
        frames = []
        for frame in gui_frames:
            frames.append(frame(self))
        return frames

    def change_frame(self, frame_id):
        self.frames[self.selected_frame].grid_forget()
        frame = self.frames[frame_id]
        frame.grid(**frame.position)
        self.selected_frame = frame_id
