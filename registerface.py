#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import LabelFrame, StringVar, Label, Button, GROOVE, Tk


class registerface(LabelFrame):
# Utilities ====================================================================

    def mkLabel(self, T, r, c):
        if isinstance(T, type(StringVar())):
            R = Label(self, textvariable = T)
        else:
            R = Label(self, text = T)
        R.grid(row=r, column=c)
        return R

    def mkStringVar(self, s):
        R = StringVar()
        R.set(s)
        return R

    def mkButton(self, t, r, c, rs=1, cs=1):
        R = Button(self, text=t)
        R.grid( row=r, column=c, rowspan=rs, columnspan=cs, sticky="wens")
        return R

    def mkLabelList(self, SV, r):
        R = []
        for i in self.RANGE:
            R.append(self.mkLabel(SV[i], r, i+1))
        return R

# Makers =======================================================================

    def mkTagLabels(self):
        self.Alabel  = self.mkLabel("A",  0, 0)
        self.Blabel  = self.mkLabel("B",  1, 0)
        self.Clabel  = self.mkLabel("C",  2, 0)
        self.Dlabel  = self.mkLabel("D",  3, 0)
        self.M1label = self.mkLabel("M1", 4, 0)
        self.M2label = self.mkLabel("M2", 5, 0)
        self.Xlabel  = self.mkLabel("X",  6, 0)
        self.Ylabel  = self.mkLabel("Y",  7, 0)

    def mkRegister(self):
        self.A  = [ self.mkStringVar("0") for unused_i in self.RANGE ]
        self.B  = [ self.mkStringVar("0") for unused_i in self.RANGE ]
        self.C  = [ self.mkStringVar("0") for unused_i in self.RANGE ]
        self.D  = [ self.mkStringVar("0") for unused_i in self.RANGE ] 
        self.M1 = [ self.mkStringVar("0") for unused_i in self.RANGE ] 
        self.M2 = [ self.mkStringVar("0") for unused_i in self.RANGE ] 
        self.X  = [ self.mkStringVar("0") for unused_i in self.RANGE ] 
        self.Y  = [ self.mkStringVar("0") for unused_i in self.RANGE ] 
        
        self.REGISTER = [self.A, self.B, self.C, self.D, \
                         self.M1, self.M2, self.X, self.Y]

    def mkLoadButtons(self):
        self.AloadButton  = self.mkButton("load A",  0, 9)
        self.BloadButton  = self.mkButton("load B",  1, 9)
        self.CloadButton  = self.mkButton("load C",  2, 9)
        self.DloadButton  = self.mkButton("load D",  3, 9)
        self.M1loadButton = self.mkButton("load M1", 4, 9)
        self.M2loadButton = self.mkButton("load M2", 5, 9)
        self.XloadButton  = self.mkButton("load X",  6, 9)
        self.YloadButton  = self.mkButton("load Y",  7, 9)

        self.XYloadButton = self.mkButton("load XY", 7, 11)

    def mkSelectButtons(self):
        self.AselectButton  = self.mkButton("select A",  0, 10)
        self.BselectButton  = self.mkButton("select B",  1, 10)
        self.CselectButton  = self.mkButton("select C",  2, 10)
        self.DselectButton  = self.mkButton("select D",  3, 10)
        self.M1selectButton = self.mkButton("select M1", 4, 10)
        self.M2selectButton = self.mkButton("select M2", 5, 10)
        self.XselectButton  = self.mkButton("select X",  6, 10)
        self.YselectButton  = self.mkButton("select Y",  7, 10)
        
        self.MselectButton  = self.mkButton("select M",  5, 11, 1, 2)
        self.XYselectButton = self.mkButton("select XY", 7, 12)

    def mkRegisterLabels(self):
        self.Alabels  = self.mkLabelList(self.A,  0)
        self.Blabels  = self.mkLabelList(self.B,  1)
        self.Clabels  = self.mkLabelList(self.C,  2)
        self.Dlabels  = self.mkLabelList(self.D,  3)
        self.M1labels = self.mkLabelList(self.M1, 4)
        self.M2labels = self.mkLabelList(self.M2, 5)
        self.Xlabels  = self.mkLabelList(self.X,  6)
        self.Ylabels  = self.mkLabelList(self.Y,  7)

    def mkHaltButton(self):
        self.HALTbutton = Button(self)
        self.HALTbutton.config(text = "HALT")
        self.HALTbutton.config(fg = "red")
        self.HALTbutton.config(command =  self.quit)
        self.HALTbutton.grid(row=0, column=11, columnspan=2, \
                             rowspan=5, sticky="wens")

# ===== gets ===================================================================

    def getRegisters(self):
        return self.REGISTER

# ===== Initialization =========================================================

    def __init__(self, x):
        LabelFrame.__init__(self, x)
        self.RANGE = range(8)
        self.config(relief=GROOVE)
        self.config(borderwidth=2)
        self.config(text = "Register")
        self.config(labelanchor = "n")

        self.mkTagLabels()
        self.mkRegister()
        self.mkLoadButtons()
        self.mkSelectButtons()        
        self.mkRegisterLabels()
        self.mkHaltButton()

        self.pack()

if __name__ == '__main__':
    root = Tk()
    rf = registerface(root)
    root.mainloop()

