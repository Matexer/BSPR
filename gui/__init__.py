import tkinter as tk
from .TopWindow import TopWindow


def start():
    root = tk.Tk()
    top = TopWindow(root)
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
    root.mainloop()
