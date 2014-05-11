#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import LabelFrame, StringVar, Label, Button, Tk, GROOVE


class memoryface(LabelFrame):

# Support ======================================================================

	def mkLabel(self, T, r, c, rs=1, cs=1):
		if isinstance(T, type(StringVar())):
			R = Label(self, textvariable = T)
		else:
			R = Label(self, text = T)
		R.grid(row=r, column=c, rowspan=rs, columnspan=cs)
		return R
	
	def mkStringVar(self, s):
		R = StringVar()
		R.set(s)
		return R
	
	def mkLabelList(self, SV, r):
		R = []
		for i in range(8):
			R.append(self.mkLabel(SV[i], r, i+2))
		return R

	def mkButton(self, t, r, c, rs=1, cs=1):
		R = Button(self, text=t)
		R.grid( row=r, column=c, rowspan=rs, columnspan=cs, sticky="wens")
		return R

	def readMemory(self):
		return self.CURRENT

# Initialization ===============================================================

	def __init__(self, x):
		LabelFrame.__init__(self, x)
		self.config(relief=GROOVE)
		self.config(borderwidth=2)
		self.config(text = "Memory")
		self.config(labelanchor = "n")

		self.READ = self.mkButton("mem read", 0, 0)
		self.WRITE = self.mkButton("mem write", 0, 1)

		self.CURRENT  = [ self.mkStringVar("0") for unused_i in range(8) ]
		self.CURRENTlabels  = self.mkLabelList(self.CURRENT, 0)

		self.pack()

# Test =========================================================================

if __name__ == '__main__':
	root = Tk()
	mf = memoryface(root)
	root.mainloop()



