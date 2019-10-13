#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    WiCC (Wifi Cracking Camp)
    Second version of the original WiCC tool at https://github.com/pabloibiza/WiCC
    GUI tool for wireless pentesting on WEP and WPA/WPA2 networks.
    Project developed by Pablo Sanz Alguacil, Miguel Yanes Fernández.
"""

from tkinter import messagebox


class PopUpWindow:

    @staticmethod
    def info(subject, text):
        messagebox.showinfo(subject, text)

    @staticmethod
    def warning(subject, text):
        messagebox.showwarning(subject, text)

    @staticmethod
    def error(subject, text):
        messagebox.showerror(subject, text)

    @staticmethod
    def yesno(subject, text):
        return messagebox.askyesno(subject, text)

    @staticmethod
    def okcancel(subject, text):
        return messagebox.askokcancel(subject, text)


