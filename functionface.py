#!/usr/bin/python


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import Frame, StringVar, Button, GROOVE, Label, Tk
#import tkFont

class functionface(Frame):

    def mkStringVar(self, s):
        R = StringVar()
        R.set(s)
        return R

    def mkFunctionButton(self, sv, r, c):
        R = Button(self, textvariable=sv)
        R.grid(row=r, column=c)
        return R

    def getFunction(self):
        return self.FUNCTION

    def __init__(self, x):
        Frame.__init__(self, x)
#        self.default_font = tkFont.nametofont("TkDefaultFont")
#        self.default_font.configure(family="Helvetica",size=10) 
        self.config(relief=GROOVE)
        self.config(borderwidth=2)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)

        self.F0label = Label(self, text="F0").grid(row=0, column=0)
        self.F1label = Label(self, text="F1").grid(row=0, column=1)
        self.F2label = Label(self, text="F2").grid(row=0, column=2)

        self.F0 = self.mkStringVar("0")
        self.F1 = self.mkStringVar("0")
        self.F2 = self.mkStringVar("0")

        self.FUNCTION = [self.F0, self.F1, self.F2]

        self.F0button = self.mkFunctionButton(self.F0, 1, 0)
        self.F1button = self.mkFunctionButton(self.F1, 1, 1)
        self.F2button = self.mkFunctionButton(self.F2, 1, 2)

        self.FUNCTIONbuttons = [self.F0button, self.F1button, self.F2button]

        self.pack()

if __name__ == '__main__':
    root = Tk()
    ff = functionface(root)
    root.mainloop()



