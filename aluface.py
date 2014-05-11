#!/usr/bin/python


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import LabelFrame, StringVar, Label, Button, GROOVE, Tk


class aluface(LabelFrame):
# Utilities ====================================================================

    def mkStringVar(self, s):
        r = StringVar()
        r.set(s)
        return r

    def mkLabel(self, T, r, c):
        if isinstance(T, type(StringVar())):
            R = Label(self, textvariable = T)
        else:
            R = Label(self, text = T)
        R.grid(row=r, column=c)
        return R

    def mkLabelList(self, SV, r):
        R = []
        for i in self.RANGE:
            R.append(self.mkLabel(SV[i], r, i+1))
        return R

# Makers =======================================================================

    def mkLOAD(self):
        self.LOADbutton = Button(self)
        self.LOADbutton.config(text = "Load Result to Data Bus")
        self.LOADbutton.grid(row=0, column=0, columnspan=9)
    
    def mkTagLabels(self):
        self.RESULTlabel = self.mkLabel("RESULT", 1, 0)
        self.ADDlabel    = self.mkLabel("ADD",    2, 0)
        self.INClabel    = self.mkLabel("INC",    3, 0)
        self.ANDlabel    = self.mkLabel("AND",    4, 0)
        self.ORlabel     = self.mkLabel("OR",     5, 0)
        self.XORlabel    = self.mkLabel("XOR",    6, 0)
        self.NOTlabel    = self.mkLabel("NOT",    7, 0)
        self.SHLlabel    = self.mkLabel("SHL",    8, 0)
        self.CLRlabel    = self.mkLabel("CLR",    9, 0)
        
        self.tagLabels = [self.ADDlabel, self.INClabel, self.ANDlabel, \
                          self.ORlabel, self.XORlabel, self.NOTlabel, \
                          self.SHLlabel, self.CLRlabel]

    def mkRegisters(self):
        self.RESULT =   [ self.mkStringVar("0") for unused_i in self.RANGE]
        self.ADD    =   [ self.mkStringVar("0") for unused_i in self.RANGE]
        self.INC    =   [ self.mkStringVar("0") for unused_i in self.RANGE]
        self.AND    =   [ self.mkStringVar("0") for unused_i in self.RANGE]
        self.OR     =   [ self.mkStringVar("0") for unused_i in self.RANGE]
        self.XOR    =   [ self.mkStringVar("0") for unused_i in self.RANGE]
        self.NOT    =   [ self.mkStringVar("0") for unused_i in self.RANGE]
        self.SHL    =   [ self.mkStringVar("0") for unused_i in self.RANGE]
        self.CLR    =   [ self.mkStringVar("0") for unused_i in self.RANGE]

        self.ALUregisters  = [self.ADD, self.INC, self.AND, \
                         self.OR, self.XOR, self.NOT, self.SHL, self.CLR]

    def mkRegisterLabels(self):
        self.RESULTlabels = self.mkLabelList(self.RESULT, 1)
        self.ADDlabels    = self.mkLabelList(self.ADD,    2)
        self.INClabels    = self.mkLabelList(self.INC,    3)
        self.ANDlabels    = self.mkLabelList(self.AND,    4)
        self.ORlabels     = self.mkLabelList(self.OR,     5)
        self.XORlabels    = self.mkLabelList(self.XOR,    6)
        self.NOTlabels    = self.mkLabelList(self.NOT,    7)
        self.SHLlabels    = self.mkLabelList(self.SHL,    8)
        self.CLRlabels    = self.mkLabelList(self.CLR,    9)
        
        self.registerLabels = [self.ADDlabels, self.INClabels, \
                               self.ANDlabels, self.ORlabels, \
                               self.XORlabels, self.NOTlabels, \
                               self.SHLlabels, self.CLRlabels]

    def addColor(self):
        self.RESULTlabel.config(fg="red")

        for i in self.RANGE:
            self.RESULTlabels[i].config(fg="red")

        self.ADDlabel.config(fg="red")
        
        for i in self.RANGE:
            self.ADDlabels[i].config(fg="red")        

# ===== sets ===================================================================



# ===== gets ===================================================================

    def getResult(self):
        return self.RESULT

    def getALUregisters(self):
        return self.ALUregisters

# ===== Initialization =========================================================

    def __init__(self, x):
        LabelFrame.__init__(self, x)
        self.config(relief=GROOVE)
        self.config(borderwidth=2)
        self.config(text = "ALU")
        self.config(labelanchor = "n")
        self.RANGE = range(8)
        self.mkLOAD()
        self.mkTagLabels()
        self.mkRegisters()
        self.mkRegisterLabels()
        self.addColor()
        self.pack()

# ===== Test ===================================================================

if __name__ == '__main__':
    root = Tk()
    cf = aluface(root)
    #cf.pack()
    root.mainloop()


