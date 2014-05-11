#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from decoder import decoder
from decoderface import decoderface
from Tkinter import Tk


class DecoderTest:
    def __init__(self):
        root = Tk()
        root.geometry("400x175+400+225")

        self.decoder = decoder()
        self.decoder_face = decoderface(root)
        
        self.decoder_face.runButton.config(command = self.decoder.decodeAll)
        self.decoder_face.randomButton.config(command = self.decoder.decodeRandom)

        root.mainloop()

if __name__ == '__main__':
    dt = DecoderTest()









