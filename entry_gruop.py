import tkinter as tk
from tkinter import ttk


class EntryGroup:

    def __init__(self, master: object, vals: dict = {}, title: str = None, direct: str = "v"):
        """
        direction -> "v" or "h"
        """
        self.main = None
        self.__entries = {}
        self.__setup_mainframe(master, title)
        self.__setup_entries(vals, direct)

    def setTitle(self, title: str):
        self.__setup_entries(self.__vals, self.__direct)

    def setValues(self, vals: dict):
        self.__setup_entries(vals, self.__direct)

    def setDirection(self, direct: str):
        """
        direct -> "v" or "h"
        """
        self.__setup_entries(self.__vals, direct)

    def setLabelGroupStyle(self, styleTag: str):
        for val in self.__entries:
            self.__entries[val][0].config(style=styleTag)

    def setLabelStyle(self, label: str, styleTag: str):
        self.__entries[label][0].config(style=styleTag)

    def setLabelWidth(self, width: int):
        for val in self.__entries:
            self.__entries[val][0].config(width=width)

    def setEntryGroupStyle(self, styleTag: str):
        for val in self.__entries:
            self.__entries[val][1].config(style=styleTag)

    def setEntryStyle(self, label: str, styleTag: str):
        self.__entries[label][1].config(style=styleTag)

    def setEntryWidth(self, width: int):
        for val in self.__entries:
            self.__entries[val][1].config(width=width)

    def getValues(self) -> dict:
        result = {}
        for val in self.__entries:
            result[val] = self.__entries[val][1].get()
        return result

    def disable(self, label: str, onoff: bool):
        if onoff == True:
            state = "disable"
        else:
            state = "normal"
        self.__entries[label][0].config(state=state)
        self.__entries[label][1].config(state=state)

    def __setup_mainframe(self, master: object, title: str):
        self.__master = master
        self.__title = title
        if not self.main == None:
            self.main.destroy()
        if title == None:
            self.main = ttk.Frame(master)
        else:
            self.main = ttk.LabelFrame(master, text=title)

    def __setup_entries(self, vals: dict, direct: str):
        if not self.__entries == {}:
            for val in self.__entries:
                self.__entries[val][0].destroy()
                self.__entries[val][1].destroy()
        self.__vals = vals
        self.__direct = direct
        self.__entries = {}
        row, column = 0, 0
        for val in vals:
            label = ttk.Label(self.main, text=val)
            entry = ttk.Entry(self.main)
            entry.insert(tk.END, str(vals[val]))
            label.grid(row=row, column=column)
            entry.grid(row=row, column=column+1)
            self.__entries[val] = [label, entry]
            if direct == "h":
                column += 2
            else:
                row += 1
