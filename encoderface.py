#!/usr/bin/python2.7

# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the
# GNU General Public License version 3.


from Tkinter import LabelFrame, GROOVE, Tk, StringVar, \
    Entry, Button, Label
#import tkFont


class encoderface(LabelFrame):

    def __init__(self, x):
        LabelFrame.__init__(self, x)       
#        self.default_font = tkFont.nametofont("TkDefaultFont")
#        self.default_font.configure(family="Helvetica",size=12)
        self.config(relief=GROOVE)
        self.config(borderwidth=2, padx=5, pady=5)
        self.config(text = "Encoder")
        self.config(labelanchor = "n")

        self.INSTRUCTION = StringVar()
        self.INSTRUCTION.set("Instruction")
        self.eval = StringVar()
        self.eval.set("Evaluation")

        self.codeEntry = Entry(self, textvariable=self.INSTRUCTION)

        #self.codeEntry.configure(font=("Helvetica", 12), width=40)
        self.codeEntry.configure(width=40)

        self.codeButton = Button(self, text="Compile")

        self.VHPL = Label(self, text="VHPL")

        self.codeButton.grid(row=0, column=0, rowspan=4, sticky="wens")

        self.VHPL.grid(row=0, column=1, sticky="wens")
        self.VHPL.config(relief=GROOVE, borderwidth=2)
        
        self.codeEntry.grid(row=1, column=1, sticky="wens")
        self.codeEntry.config(fg="green", bg="black")
        
        self.pack()

if __name__ == "__main__":
    root = Tk()
    ef = encoderface(root)
    root.mainloop()
