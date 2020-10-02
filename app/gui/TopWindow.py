import tkinter as tk
from .frames import load_frames, LeftMenuFrame, TopMenuFrame
from .configure import *


class TopWindow(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.configure(background=TW_BG)
        self.pack(fill="both", expand=1)

        left_menu_frame = LeftMenuFrame(self)
        left_menu_frame.pack(side="left", fill="y")
        top_menu_frame = TopMenuFrame(self)
        top_menu_frame.pack(side="top", fill="x")

        self.selected_frame = 0
        self.frames = load_frames(self)
        self.frames[self.selected_frame].pack(fill="both", expand=1)

    def change_frame(self, frame_id):
        self.frames[self.selected_frame].pack_forget()
        self.frames[frame_id].pack(fill="both", expand=1)
        self.selected_frame = frame_id
