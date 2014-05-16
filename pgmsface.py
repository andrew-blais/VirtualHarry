#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import LabelFrame, GROOVE, StringVar, OptionMenu, Button, Tk
#import tkFont


class pgmsface(LabelFrame):


    def __init__(self, x):
        LabelFrame.__init__(self, x)
#        self.default_font = tkFont.nametofont("TkDefaultFont")
#        self.default_font.configure(family="Helvetica",size=10)         
        self.config(relief=GROOVE)
        self.config(borderwidth=2)
        self.config(text = "Testing")
        self.config(labelanchor = "n")

        self.var = StringVar(self)
        self.var.set("testGOTOpgm")

        self.choices = ["testGOTOpgm", \
                        "testSETMpgm", \
                        "testLOADpgm", \
                        "testSETABpgm", \
                        "testINCpgm", \
                        "testALUpgm", \
                        "testMOVpgm", \
                        "testCBpgm1", \
                        "testCBpgm2", \
                        "subtractPGM", \
                        "multiplyPGM"]

        self.button = Button(self, text="Load Test")
        self.button.grid(row=0, column=0)
        
        self.option = OptionMenu(self, self.var, *self.choices)
        # Use * when you're not sure how many arguments might be passed to 
        # your function. This makes it possible to pass an arbitrary number 
        # of arguments to your function.
        
        self.option.grid(row=0, column=1)
        
        self.pack()

if __name__ == '__main__':
    root = Tk()
    pf = pgmsface(root)
    root.mainloop()
    

