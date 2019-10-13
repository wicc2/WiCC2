#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    WiCC (Wifi Cracking Camp)
    Second version of the original WiCC tool at https://github.com/pabloibiza/WiCC
    GUI tool for wireless pentesting on WEP and WPA/WPA2 networks.
    Project developed by Pablo Sanz Alguacil, Miguel Yanes Fernández.
"""
import webbrowser
from tkinter import *
from tkinter import Frame, Button, Label, RIGHT


class About:
    logo = "/resources/icon_medium.png"

    def __init__(self, main_directory):
        self.logo = main_directory + self.logo
        self.build_window()
        self.root.mainloop()

    def build_window(self):
        """
        Generates the window.

        :author: Pablo Sanz Alguacil
        """

        self.root = Toplevel()
        self.root.geometry('460x300')
        self.root.resizable(width=False, height=False)
        self.root.title('About')

        # LABEL - INFO
        self.label_info = Label(self.root, pady=15,
                                text="Developed as the Group Project for 3rd year of the Bachelor "
                                     "\nof Science in Computing in Digital Forensics and Cyber Security "
                                     "\nat the Technological University Dublin."
                                     "\n")

        self.label_info.pack()

        self.button = Button(self.root, text="Project page", command=self.open_link)
        self.button.pack()

        self.frame = Frame(self.root)
        self.frame.pack()

        photo = PhotoImage(file=self.logo)
        photo_label = Label(self.frame, image=photo)
        photo_label.image = photo
        photo_label.pack(side=LEFT)

        self.label_collaborators = Label(self.frame, text="\tPablo Sanz Alguacil"
                                                          "\n\tMiguel Yanes Fernández")
        self.label_collaborators.pack(side=RIGHT)

    def open_link(event):
        """
        Opens the URL on a new tab in the default web browser.

        :author: Pablo Sanz Alguacil
        """

        url = "http://www.github.com/MiguelYanes/WiCC2"
        webbrowser.open_new_tab(url)
