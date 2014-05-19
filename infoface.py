#!/usr/bin/python2.7

# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the
# GNU General Public License version 3.


from Tkinter import LabelFrame, GROOVE, Tk, Button
#import tkFont


class infoface(LabelFrame):

    def __init__(self, x):
        LabelFrame.__init__(self, x)       
#        self.default_font = tkFont.nametofont("TkDefaultFont")
#        self.default_font.configure(family="Helvetica",size=12)
        self.config(relief=GROOVE)
        self.config(borderwidth=2, padx=5, pady=5)
        self.config(text = "Information")
        self.config(labelanchor = "n")

        self.readmeButton = Button(self, text="README", fg="red")
        self.readmeButton.grid(row=0, column=0, sticky="wens")

        self.pack()

if __name__ == "__main__":
    root = Tk()
    iface = infoface(root)
    root.mainloop()
    
    
    