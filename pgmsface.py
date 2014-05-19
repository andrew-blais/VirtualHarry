#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import LabelFrame, GROOVE, Button, Tk, StringVar, Label
from tkFileDialog import askopenfilename
#import tkFont


class pgmsface(LabelFrame):

    def getPGMfileName(self):
        options = {'filetypes': [('pgm files', '.pgm')]}
        f = askopenfilename(**options)
        g = f.split('/')
        self.filenameVar.set(g[len(g) - 1])
        return f

    def __init__(self, x):
        LabelFrame.__init__(self, x)
#        self.default_font = tkFont.nametofont("TkDefaultFont")
#        self.default_font.configure(family="Helvetica",size=10)         
        self.config(relief=GROOVE)
        self.config(borderwidth=2)
        self.config(text = "Testing")
        self.config(labelanchor = "n")

        self.loadPGMbutton = Button(self, text="Load PGM")
        self.loadPGMbutton.grid(row=0, column=0)
        
        self.filenameVar = StringVar()
        self.filenameVar.set("*****.pgm")
        
        self.fileNameLabel = Label(self, textvariable=self.filenameVar)
        self.fileNameLabel.config(relief=GROOVE, borderwidth=2, width=18)
        self.fileNameLabel.grid(row=0, column=1)

        self.pack()

if __name__ == '__main__':
    root = Tk()
    pf = pgmsface(root)
    root.mainloop()
    

