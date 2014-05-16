#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import LabelFrame, StringVar, Label, Button, GROOVE, Tk
#import tkFont


class controlface(LabelFrame):
# Support ======================================================================

    def mkLabel(self, T, r, c, rs=1, cs=1):
        if isinstance(T, type(StringVar())):
            R = Label(self, textvariable = T)
        else:
            R = Label(self, text = T)
        R.grid(row=r, column=c, rowspan=rs, columnspan=cs)
        return R

    def mkStringVar(self, s):
        R = StringVar()
        R.set(s)
        return R
    
    def mkLabelList(self, SV, r):
        R = []
        for i in self.RANGE:
            R.append(self.mkLabel(SV[i], r, i+1))
        return R
    
    def mkButton(self, t, r, c, rs=1, cs=1):
        R = Button(self, text=t)
        R.grid( row=r, column=c, \
                rowspan = rs, columnspan = cs, \
                sticky="wens")
        return R

    def getRegisters(self):
        return self.REGISTERS
    
    def getInstruction(self):
        return self.INST

# Makers =======================================================================

    def mkTagLabels(self):
        self.J1label       = self.mkLabel("   J1 ",         0, 0)
        self.J2label       = self.mkLabel("   J2 ",         1, 0)
        self.INSTlabel     = self.mkLabel(" Inst ",         2, 0)
        self.PC1label      = self.mkLabel("  PC1 ",         3, 0)
        self.PC2label      = self.mkLabel("  PC2 ",         4, 0)
        self.IncrUnitlabel = self.mkLabel(" Incr \nUnit ",  5, 0, 2, 1)
        self.Inc1label     = self.mkLabel(" Inc1 ",         7, 0)
        self.Inc2label     = self.mkLabel(" Inc2 ",         8, 0)

    def mkRegister(self):
        self.J1        = [ self.mkStringVar("0") for unused_i in self.RANGE ]
        self.J2        = [ self.mkStringVar("0") for unused_i in self.RANGE ]
        self.INST      = [ self.mkStringVar("0") for unused_i in self.RANGE ]
        self.PC1       = [ self.mkStringVar("0") for unused_i in self.RANGE ]
        self.PC2       = [ self.mkStringVar("0") for unused_i in self.RANGE ]
        self.IncUnit1  = [ self.mkStringVar("0") for unused_i in self.RANGE ]
        self.IncUnit2  = [ self.mkStringVar("0") for unused_i in self.RANGE ]
        self.Inc1      = [ self.mkStringVar("0") for unused_i in self.RANGE ]
        self.Inc2      = [ self.mkStringVar("0") for unused_i in self.RANGE ]
        
        self.REGISTERS = [self.J1, self.J2, self.PC1, \
                          self.PC2, self.IncUnit1, self.IncUnit2, \
                          self.Inc1, self.Inc2 ]

    def mkRegisterLabels(self):
        self.J1labels        = self.mkLabelList(self.J1,       0)
        self.J2labels        = self.mkLabelList(self.J2,       1)        
        self.INSTlabels      = self.mkLabelList(self.INST,     2)
        self.PC1labels       = self.mkLabelList(self.PC1,      3)
        self.PC2labels       = self.mkLabelList(self.PC2,      4)
        self.IncrUnit1labels = self.mkLabelList(self.IncUnit1, 5)
        self.IncrUnit2labels = self.mkLabelList(self.IncUnit2, 6)
        self.Inc1labels      = self.mkLabelList(self.Inc1,     7)
        self.Inc2labels      = self.mkLabelList(self.Inc2,     8)
                
    def mkLoadButtons(self):
        self.J1loadButton   = self.mkButton("load J1",   0, 9)
        self.J2loadButton   = self.mkButton("load J2",   1, 9)
        self.INSTloadButton = self.mkButton("load Inst", 2, 9, 1, 2)
        self.PCloadButton   = self.mkButton("load PC",   3, 9, 2, 1)
        self.INCloadButton  = self.mkButton("load INC",  7, 9, 2, 1)

    def mkSelectButtons(self):
        self.JselectButton   = self.mkButton("select J",   0, 10, 2, 1)
        self.PCselectButton  = self.mkButton("select PC",  3, 10, 2, 1)
        self.INCselectButton = self.mkButton("select INC", 7, 10, 2, 1)

# Initialization ===============================================================

    def __init__(self, x):
        LabelFrame.__init__(self, x)
#        self.default_font = tkFont.nametofont("TkDefaultFont")
#        self.default_font.configure(family="Helvetica",size=10)

        self.RANGE = range(8)
        self.config(text = "Control Unit")
        self.config(labelanchor = "n")

        self.config(relief=GROOVE)
        self.config(borderwidth=2)

        self.mkTagLabels()
        self.mkRegister()
        self.mkRegisterLabels()
        self.mkLoadButtons()
        self.mkSelectButtons()

        self.pack()

if __name__ == '__main__':
    root = Tk()
    cf = controlface(root)
    root.mainloop()
