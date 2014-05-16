#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import LabelFrame, Button, GROOVE, Tk
#import tkFont

class decoderface(LabelFrame):


    def mkButtons(self):
        self.runButton = Button(self, text="RUN")
        self.runButton.grid(row=0, column=0, sticky="wens")

        self.stepButton = Button(self, text="STEP")
        self.stepButton.grid(row=0, column=1, sticky="wens")

        self.noStepButton = Button(self, text="NOSTEP")
        self.noStepButton.grid(row=0, column=2, sticky="wens")

        self.pack()

    def __init__(self, x):
        LabelFrame.__init__(self, x)
#        self.default_font = tkFont.nametofont("TkDefaultFont")
#        self.default_font.configure(family="Helvetica",size=10)        
        self.config(relief=GROOVE)
        self.config(borderwidth=2)
        self.config(text="Decoder")
        self.mkButtons()

if __name__ == '__main__':
    root = Tk()
    df = decoderface(root)
    #df.grid(row=0, column=0)
    root.mainloop()




