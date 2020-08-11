import tkinter as tk
import os
import platform
import subprocess
from gui.configure import *
from gui.elements import TopMenuButton
from globals import FUELS_FOLDER


class TopMenuFrame(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)
        self.configure(background=TMF_BG)

        self.fuel_list_btn = TopMenuButton(self)
        self.fuel_list_btn.pack(side="left")
        self.fuel_list_btn.configure(text='Lista paliw',
                                     command=lambda: top.change_frame(0))

        self.survey_list_btn = TopMenuButton(self)
        self.survey_list_btn.pack(side="left")
        self.survey_list_btn.configure(text='Lista pomiarów',
                                       command=lambda: top.change_frame(2))

        self.configure_btn = TopMenuButton(self)
        self.configure_btn.pack(side="right")
        self.configure_btn.configure(text='Konfiguracja',
                                     command=lambda: top.change_frame(4))

        self.configure_btn = TopMenuButton(self)
        self.configure_btn.pack(side="right")
        self.configure_btn.configure(text='Baza danych',
                                     command=lambda: self.open_database_folder())

    @staticmethod
    def open_database_folder():
        path = os.getcwd() + "/" + FUELS_FOLDER
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
