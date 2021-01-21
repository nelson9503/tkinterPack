import tkinter as tk
from tkinter import ttk


class RadioGroup:

    def __init__(self, master: object, vals: list = [], title: str = None, direct: str = "v"):
        """
        direction -> "v" or "h"
        """
        self.main = None
        self.__radios = {}
        self.__setup_mainframe(master, title)
        self.__setup_radios(vals, direct)

    def setValues(self, vals: list):
        self.__setup_radios(vals, self.__direct)

    def setDirection(self, direct: str):
        """
        direct -> "v" or "h"
        """
        self.__setup_radios(self.__vals, direct)

    def setWidth(self, width: int):
        for order in self.__radios:
            self.__radios[order][0].config(width=width)

    def getValues(self) -> str:
        result = self.__radios[self.__checkvar.get()][1]
        return result

    def setGroupStyle(self, styleTag: str):
        for order in self.__radios:
            self.__radios[order][0].config(style=styleTag)

    def setStyle(self, order: int, styleTag: str):
        self.__radios[order][0].config(style=styleTag)

    def disable(self, option: str, onoff: bool):
        if onoff == True:
            state = "disable"
        else:
            state = "normal"
        index = self.__vals.index(option)
        self.__radios[index][0].config(state=state)

    def __setup_mainframe(self, master: object, title: str):
        self.__master = master
        self.__title = title
        if not self.main == None:
            self.main.destroy()
        if title == None:
            self.main = ttk.Frame(master)
        else:
            self.main = ttk.LabelFrame(master, text=title)

    def __setup_radios(self, vals: list, direct: str):
        if not self.__radios == {}:
            for order in self.__radios:
                self.__radios[order][0].destroy()
        self.__vals = vals
        self.__direct = direct
        self.__radios = {}
        self.__checkvar = tk.IntVar(value=0)
        row, column = 0, 0
        for i in range(len(vals)):
            val = vals[i]
            radio = ttk.Radiobutton(
                self.main, text=val, variable=self.__checkvar, value=i)
            radio.grid(row=row, column=column)
            self.__radios[i] = [radio, val]
            if direct == "h":
                column += 1
            else:
                row += 1
