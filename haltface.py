#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import Frame, GROOVE, Button, Tk


class haltface(Frame):

    def __init__(self, x):
        Frame.__init__(self, x)
        self.config(relief=GROOVE)
        self.config(borderwidth=2)

        self.HALTbutton = Button(self)
        self.HALTbutton.config(text = "HALT")
        self.HALTbutton.config(fg = "red")
        self.HALTbutton.config(command =  self.quit)
        self.HALTbutton.grid(row=0, column=0, sticky="wens")

        self.pack()

if __name__ == '__main__':
    root = Tk()
    hf = haltface(root)
    root.mainloop()

