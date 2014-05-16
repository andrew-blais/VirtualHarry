#!/usr/bin/python2.7

from Tkinter import LabelFrame, StringVar, GROOVE, Button, Tk
from sys import argv
#import tkFont


class addressbusface(LabelFrame):

    def mkStringVar(self, s):
        r = StringVar()
        r.set(s)
        return r

    def getAddressBus(self):
        return self.AB

    def __init__(self, x):
        LabelFrame.__init__(self, x)
#        self.default_font = tkFont.nametofont("TkDefaultFont")
#        self.default_font.configure(family="Helvetica",size=10)
        self.config(relief=GROOVE)
        self.config(borderwidth=2)
        self.config(text = "16 bit Address Bus")
        self.config(labelanchor = "n")

        self.AB = []
        self.ABbuttons = []

        for i in range(16):
            self.AB.append(self.mkStringVar("0"))
            self.ABbuttons.append(Button(self, textvariable=self.AB[i]))
            self.ABbuttons[i].grid(row=0, column=i)
            
        self.pack()

if __name__ == '__main__':
    root = Tk()
    if len(argv) > 1: 
        root.geometry(argv[1])
    abf = addressbusface(root)
    #abf.grid(row=0, column=0)
    root.mainloop()



