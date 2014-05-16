#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import Frame, Label, StringVar, GROOVE, Tk
#import tkFont


class statesface(Frame):

    def set(self, C, Z, S):
        self.CARRY.set(str(C))
        self.ZERO.set(str(Z))
        self.SIGN.set(str(S))

    def getCYZS(self):
        return [self.CARRY, self.ZERO, self.SIGN]

    def mkStateLabels(self):
        self.CARRYtag = Label(self, text = " carry ").grid(row=0, column=0)
        self.ZEROtag = Label(self, text =  "  zero ").grid(row=0, column=1)
        self.SIGNtag = Label(self, text =  "  sign ").grid(row=0, column=2)

        self.CARRY = StringVar()
        self.ZERO = StringVar()
        self.SIGN = StringVar()
        self.CARRY.set("0")
        self.ZERO.set("0")
        self.SIGN.set("0")
        
        self.CARRYlabel = Label(self, textvariable = self.CARRY).grid(row=1, column=0)
        self.ZEROlabel = Label(self, textvariable = self.ZERO).grid(row=1, column=1)
        self.SIGNlabel = Label(self, textvariable = self.SIGN).grid(row=1, column=2)

    def __init__(self, x):
        Frame.__init__(self, x)
#        self.default_font = tkFont.nametofont("TkDefaultFont")
#        self.default_font.configure(family="Helvetica",size=10) 
        self.config(relief=GROOVE)
        self.config(borderwidth=2)
        self.mkStateLabels()
        self.pack()

if __name__ == '__main__':
    root = Tk()
    sf = statesface(root)
    root.mainloop()


