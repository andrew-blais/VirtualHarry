#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import LabelFrame, GROOVE, Label, Tk, StringVar
#import tkFont


class clockface(LabelFrame):
    
    def __init__(self, x):
        LabelFrame.__init__(self, x)
#        self.default_font = tkFont.nametofont("TkDefaultFont")
#        self.default_font.configure(family="Helvetica",size=10)

        self.config(relief=GROOVE)
        self.config(borderwidth=2)
        self.config(text = "Up Time")
        self.config(labelanchor = "n")
        
        self.Hsv = StringVar()
        self.Hsv.set("")
        self.Hlabel = Label(self, textvariable = self.Hsv)
        self.Hlabel.grid(row=0, column=0, sticky="wens")
        self.Hlabel.config(font=("Courier", 14))
        
        self.Msv = StringVar()
        self.Msv.set("")
        self.Mlabel = Label(self, textvariable = self.Msv)
        self.Mlabel.grid(row=1, column=0, sticky="wens")
        self.Mlabel.config(font=("Courier", 14))
        
        self.Ssv = StringVar()
        self.Ssv.set("")
        self.Slabel = Label(self, textvariable = self.Ssv)
        self.Slabel.grid(row=2, column=0, sticky="wens")
        self.Slabel.config(font=("Courier", 14))

        self.pack()

if __name__ == '__main__':
    root = Tk()
    cf = clockface(root)
    root.mainloop()
