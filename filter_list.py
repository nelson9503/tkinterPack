import tkinter as tk
from tkinter import ttk


class FilterList:

    def __init__(self, master: object, vals: list, title: str = None):
        self.main = None
        self.__setup_mainframe(master, title)
        self.__setup_entry()
        self.__setup_listbox()
        self.__setup_label()

    def setValues(self, vals: list):
        self.vals = vals
        self.var.set("")
        self.__set_values(self.vals)

    def getValue(self):
        v = self.vals[self.list.curselection()[0]]
        return v

    def __set_values(self, vals: list):
        self.list.delete(0, tk.END)
        for i in range(len(vals)):
            self.list.insert(i, vals[i])
        self.lbl.configure(text="{} results".format(len(vals)))

    def __setup_mainframe(self, master: object, title: str):
        self.__master = master
        self.__title = title
        if not self.main == None:
            self.main.destroy()
        if title == None:
            self.main = ttk.Frame(master)
        else:
            self.main = ttk.LabelFrame(master, text=title)

    def __setup_entry(self):
        self.var = tk.StringVar()
        self.var.trace_add("write", self.__trace_entry)
        self.entry = ttk.Entry(self.main, textvariable=self.var)
        self.entry.pack(fill="x")

    def __trace_entry(self, *args, **kwargs):
        filter = self.var.get()
        vals = []
        for val in self.vals:
            if filter in val:
                vals.append(val)
        self.__set_values(vals)

    def __setup_listbox(self):
        self.list = tk.Listbox(self.main)
        self.list.pack(fill="x")

    def __setup_label(self):
        self.lbl = ttk.Label(self.main, text="0 results", anchor='e')
        self.lbl.pack(fill="x")
