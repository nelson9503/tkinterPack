import tkinter as tk
from tkinter import ttk
from .progressbar_group import ProgressbarGroup


class StepProcessGroup:

    def __init__(self, master: object, title: str = None):
        self.main = None
        self.bars = []
        self.__setup_mainframe(master, title)

    def insertBar(self, title: str = None, barWidth: int = 100):
        bar = ProgressbarGroup(self.main, title, barWidth)
        bar.main.pack(fill="both")
        self.bars.append(bar)

    def setProgress(self, index: int, percentage: float, showRound: int = 0):
        self.bars[index].setProgress(percentage, showRound)

    def setText(self, index: int, text: str):
        self.bars[index].setText(text)

    def __setup_mainframe(self, master: object, title: str):
        self.__master = master
        self.__title = title
        if not self.main == None:
            self.main.destroy()
        if title == None:
            self.main = ttk.Frame(master)
        else:
            self.main = ttk.LabelFrame(master, text=title)
