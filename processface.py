#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import LabelFrame, GROOVE, Tk, Text, Scrollbar, LEFT, \
    RIGHT, Y, END

from random import randint
from string import ascii_uppercase, ascii_lowercase
from time import sleep
from thread import start_new_thread


class processface(LabelFrame):
    
    def __init__(self, x):
        LabelFrame.__init__(self, x)
        self.config(relief=GROOVE)
        self.config(borderwidth=2)
        self.config(text = "Process")
        self.config(labelanchor = "n")
    
        self.text = Text(self, height=26, width=80)
        
        self.scroll = Scrollbar(self, command=self.text.yview)
        
        self.text.configure(yscrollcommand=self.scroll.set)
        
        self.text.pack(side=LEFT, padx=3, pady=2)

        self.scroll.pack(side=RIGHT, fill=Y, padx=3, pady=2)

        self.pack(padx=4, pady=4)

    def addText(self, t):
        self.text.insert(END, t + "\n")

    def mkRandomString(self):
        L = ascii_uppercase
        L = L + ascii_lowercase
        s = ""
        for unused_i in range(0,70):
            s = s + L[randint(0,len(L)-1)]
        return s

    def fillText(self):
        for unused_i in range(128):
            self.addText(self.mkRandomString())
            sleep(0.5)

if __name__ == '__main__':
    root = Tk()
    pf = processface(root)

    start_new_thread(pf.fillText, ())

    root.mainloop()    

    
    
    