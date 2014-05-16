#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import LabelFrame, StringVar, GROOVE, Button, Tk
#import tkFont

class databusface(LabelFrame):

    def mkStringVar(self, s):
        r = StringVar()
        r.set(s)
        return r

    def getDataBus(self):
        return self.DB

    def __init__(self, x):
        LabelFrame.__init__(self, x)
#        self.default_font = tkFont.nametofont("TkDefaultFont")
#        self.default_font.configure(family="Helvetica",size=10)        
        self.config(relief=GROOVE)
        self.config(borderwidth=2)
        self.config(text = "8 bit Data Bus")
        self.config(labelanchor = "n")
        
        self.DB = []
        self.DBbuttons = []

        for i in range(8):
            self.DB.append(self.mkStringVar("0"))
            self.DBbuttons.append(Button(self, textvariable=self.DB[i]))
            self.DBbuttons[i].grid(row=0, column=i)

        self.pack()

if __name__ == '__main__':
    root = Tk()
    dbf = databusface(root)
    #dbf.grid(row=0, column=0)
    root.mainloop()



