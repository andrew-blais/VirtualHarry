#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import LabelFrame, Button, GROOVE, Tk


class decoderface(LabelFrame):


    def mkButtons(self):
        self.subtractButton = Button(self, text = "load subtract")
        self.subtractButton.grid(row=0, column=0, sticky="wens")

        self.multiplyButton = Button(self, text = "load multiply")
        self.multiplyButton.grid(row=1, column=0, sticky="wens")

        self.testSETABButton = Button(self, text="test SETAB")
        self.testSETABButton.grid(row=2, column=0, sticky="wens")

        self.testLOADButton = Button(self, text="test LOAD")
        self.testLOADButton.grid(row=3, column=0, sticky="wens")

        self.testSETMButton = Button(self, text="test SETM")
        self.testSETMButton.grid(row=4, column=0, sticky="wens")

        self.testGOTOMButton = Button(self, text="test GOTO")
        self.testGOTOMButton.grid(row=5, column=0, sticky="wens")

        self.runButton = Button(self, text="RUN")
        self.runButton.grid(row=6, column=0, sticky="wens")

        self.stepButton = Button(self, text="STEP")
        self.stepButton.grid(row=7, column=0, sticky="wens")

        self.noStepButton = Button(self, text="NOSTEP")
        self.noStepButton.grid(row=8, column=0, sticky="wens")

    def __init__(self, x):
        LabelFrame.__init__(self, x)
        self.config(relief=GROOVE)
        self.config(borderwidth=2)
        self.config(text="Decoder")
        self.mkButtons()
        self.pack()


if __name__ == '__main__':
    root = Tk()
    df = decoderface(root)
    root.mainloop()
