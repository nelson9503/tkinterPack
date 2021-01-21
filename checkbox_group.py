import tkinter as tk
from tkinter import ttk


class CheckboxGroup:

    def __init__(self, master: object, vals: dict = {}, title: str = None, direct: str = "v"):
        """
        direction -> "v" or "h"
        """
        self.main = None
        self.__checks = {}
        self.__setup_mainframe(master, title)
        self.__setup_checkboxes(vals, direct)

    def setTitle(self, title: str):
        self.__setup_mainframe(self.__master, title)
        self.__setup_checkboxes(self.__vals, self.__direct)

    def setValues(self, vals: dict):
        self.__setup_mainframe(self.__master, self.__title)
        self.__setup_checkboxes(vals, self.__direct)

    def setDirection(self, direct: str):
        """
        direct -> "v" or "h"
        """
        self.__setup_mainframe(self.__master, self.__title)
        self.__setup_checkboxes(self.__vals, direct)

    def setGroupStyle(self, styleTag: str):
        for val in self.__checks:
            self.__checks[val][0].config(style=styleTag)

    def setStyle(self, option: str, styleTag: str):
        self.__checks[option][0].config(style=styleTag)

    def setWidth(self, width: int):
        for val in self.__checks:
            self.__checks[val][0].config(width=width)

    def getValues(self) -> dict:
        result = {}
        for val in self.__checks:
            result[val] = self.__checks[val][1].get()
        return result

    def disable(self, option: str, onoff: bool):
        if onoff == True:
            state = "disable"
        else:
            state = "normal"
        self.__checks[option][0].config(state=state)

    def __setup_mainframe(self, master: object, title: str):
        self.__master = master
        self.__title = title
        if not self.main == None:
            self.main.destroy()
        if title == None:
            self.main = ttk.Frame(master)
        else:
            self.main = ttk.LabelFrame(master, text=title)

    def __setup_checkboxes(self, vals: dict, direct: str):
        if not self.__checks == {}:
            for val in self.__checks:
                self.__checks[val][0].destroy()
                self.__checks[val][1].destroy()
        self.__vals = vals
        self.__direct = direct
        self.__checks = {}
        row, column = 0, 0
        for val in vals:
            var = tk.BooleanVar(value=vals[val])
            box = ttk.Checkbutton(self.main, text=val, variable=var)
            box.grid(row=row, column=column)
            self.__checks[val] = [box, var]
            if direct == "h":
                column += 1
            else:
                row += 1
