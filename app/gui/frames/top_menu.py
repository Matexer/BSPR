import tkinter as tk
import os
import platform
import subprocess
import time
from ..configure import FOLDER_IMG, WRENCH_IMG, TMF_BG
from ..elements import TopMenuButton
from ...globals import FUELS_FOLDER


class TopMenuFrame(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)
        self.folder_img = tk.PhotoImage(file=FOLDER_IMG).subsample(3, 3)
        self.wrench_img = tk.PhotoImage(file=WRENCH_IMG).subsample(1, 1)
        self.configure(background=TMF_BG)

        self.fuel_list_btn = TopMenuButton(self)
        self.fuel_list_btn.pack(side="left")
        self.fuel_list_btn.configure(text='Lista paliw',
                                     command=lambda: top.change_frame(0))

        self.survey_list_btn = TopMenuButton(self)
        self.survey_list_btn.pack(side="left")
        self.survey_list_btn.configure(text='Lista pomiarów',
                                       command=lambda: top.change_frame(2))

        #Disabled
        self.configure_btn = TopMenuButton(self)
        self.configure_btn.pack(side="right", ipadx=50)
        self.configure_btn.configure(text='Konfiguracja',
                                     image=self.wrench_img,
                                     compound="left",
                                     command=lambda: 1)

        self.configure_btn = TopMenuButton(self)
        self.configure_btn.pack(side="right", ipadx=45)
        self.configure_btn.configure(text='Baza danych',
                                     image=self.folder_img,
                                     compound="left",
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
        time.sleep(1)
