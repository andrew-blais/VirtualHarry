#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import Frame, GROOVE, Listbox, Scrollbar, Tk, \
    LEFT, RIGHT, Y, END


class testface(Frame):

    def __init__(self, x):
        Frame.__init__(self, x)
        self.config(relief=GROOVE)
        self.config(borderwidth=2)

        self.tests = Listbox(x, height=6, width=15)
        self.scroll = Scrollbar(x, command=self.tests.yview)
        self.tests.pack(side=LEFT)
        self.scroll.pack(side=RIGHT, fill=Y)
        for i in range(32):
            self.tests.insert(END, i)

        self.pack()

if __name__ == '__main__':
    root = Tk()
    tf = testface(root)
    root.mainloop()


