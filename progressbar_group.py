import tkinter as tk
from tkinter import ttk


class ProgressbarGroup:

    def __init__(self, master, title: str = None, barWidth: int = 100):
        self.main = None
        self.__setup_mainframe(master, title)
        self.__setup_progressbar(barWidth=barWidth)

    def setProgress(self, percentage: float, showRound: int = 0):
        if percentage > 1:
            percentage = 1
        if showRound == 0:
            per = int(percentage * 100)
        else:
            per = round(percentage * 100, showRound)
        self.bar["value"] = per
        self.bar.update()
        self.perlbl.configure(text="{}%".format(per))
    
    def setText(self, text: str):
        self.statelbl.configure(text=text)

    def __setup_mainframe(self, master: object, title: str):
        self.__master = master
        self.__title = title
        if not self.main == None:
            self.main.destroy()
        if title == None:
            self.main = ttk.Frame(master)
        else:
            self.main = ttk.LabelFrame(master, text=title)

    def __setup_progressbar(self, barWidth: int = 100):
        f = ttk.Frame(self.main)
        f.pack(fill="both")
        self.bar = ttk.Progressbar(f, orient=tk.HORIZONTAL, length=barWidth)
        self.bar.grid(row=0, column=0)
        self.perlbl = ttk.Label(f, text="0%")
        self.perlbl.grid(row=0, column=1)
        self.statelbl = ttk.Label(self.main, text="")
        self.statelbl.pack(fill="both")
