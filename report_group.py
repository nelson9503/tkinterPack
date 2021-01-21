import tkinter as tk
from tkinter import ttk


class ReportGroup:

    def __init__(self, master: object, vals: dict = {}, title: str = None, direct: str = "v"):
        """
        direction -> "v" or "h"
        """
        self.main = None
        self.__reports = {}
        self.__setup_mainframe(master, title)
        self.__setup_reports(vals, direct)

    def setValues(self, vals: dict):
        self.__setup_reports(vals, self.__direct)

    def setDirection(self, direct: str):
        """
        direct -> "v" or "h"
        """
        self.__setup_reports(self.__vals, direct)

    def setLabelGroupStyle(self, styleTag: str):
        """
        Set style for all Labels.
        """
        for val in self.__reports:
            self.__reports[val][0].config(style=styleTag)

    def setLabelStyle(self, label: str, styleTag: str):
        """
        Set style for single label.
        """
        self.__reports[label][0].config(style=styleTag)

    def setLabelWidth(self, width: int):
        for val in self.__reports:
            self.__reports[val][0].config(width=width)

    def setContentStyle(self, label: str, styleTag: str):
        self.__reports[label][1].config(style=styleTag)

    def setContentGroupStyle(self, styleTag: str):
        for val in self.__reports:
            self.__reports[val][1].config(style=styleTag)

    def setContentWidth(self, width: int):
        for val in self.__reports:
            self.__reports[val][1].config(width=width)

    def getValues(self) -> dict:
        result = {}
        for val in self.__reports:
            result[val] = self.__reports[val][1].get()
        return result

    def disable(self, label: str, onoff: bool):
        if onoff == True:
            state = "disable"
        else:
            state = "normal"
        self.__reports[label][0].config(state=state)
        self.__reports[label][1].config(state=state)

    def __setup_mainframe(self, master: object, title: str):
        self.__master = master
        self.__title = title
        if not self.main == None:
            self.main.destroy()
        if title == None:
            self.main = ttk.Frame(master)
        else:
            self.main = ttk.LabelFrame(master, text=title)

    def __setup_reports(self, vals: dict, direct: str):
        if not self.__reports == {}:
            for val in self.__reports:
                self.__reports[val][0].destroy()
                self.__reports[val][1].destroy()
        self.__vals = vals
        self.__direct = direct
        self.__reports = {}
        row, column = 0, 0
        for val in vals:
            label = ttk.Label(self.main, text=val,
                              font=('Helvetica', 10, "bold"))
            content = ttk.Label(self.main, text=str(
                vals[val]), font=('Helvetica', 10))
            label.grid(row=row, column=column)
            content.grid(row=row, column=column+1)
            self.__reports[val] = [label, content]
            if direct == "h":
                column += 2
            else:
                row += 1
