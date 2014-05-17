#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import Tk, Toplevel, Frame
from aluface import aluface
from functionface import functionface
from statesface import statesface
from registerface import registerface
from controlface import controlface
from databusface import databusface
from addressbusface import addressbusface
from memoryface import memoryface
from core import core
from decoderface import decoderface
from pgmsface import pgmsface
import pgms
from processface import processface
from time import sleep
from encoderface import encoderface


class VirtualHarry:
# Support ======================================================================

    def setSVtoV(self, sv, v):
        for i in range(len(sv)):
            sv[i].set(str(v[i]))

# Make Utilities ===============================================================

    def mkConstants(self):
        self.Range = range(8)
        self.Egnar = self.Range.reverse()
        self.Range3 = range(3)
        self.Range16 = range(16)

    def mkTopFaces(self, r):
        
        self.WHOLE = Toplevel(r)
        self.WHOLE.title("Virtual Harry")
        self.WHOLE.geometry("+70+40")
        
        self.UNITY = Frame(self.WHOLE)
        self.UNITY.grid(row=0, column=0)

        self.RF = registerface(self.UNITY)       
        self.FF = functionface(self.UNITY)
        self.SF = statesface(self.UNITY)
        self.ALUF = aluface(self.UNITY)
        self.CF = controlface(self.UNITY)
        self.EF = encoderface(self.UNITY)

        self.RF.grid(row=0,column=0, columnspan=2)
        self.FF.grid(row=1,column=0)
        self.SF.grid(row=1,column=1)
        self.ALUF.grid(row=2,column=0)
        self.CF.grid(row=2,column=1)
        self.EF.grid(row=3, column=0, columnspan=2)

        self.SEQUENCERFACE = Frame(self.WHOLE)
        self.SEQUENCERFACE.grid(row=0, column=1)

        self.ABF = addressbusface(self.SEQUENCERFACE)
        self.DF = decoderface(self.SEQUENCERFACE)
        self.DBF = databusface(self.SEQUENCERFACE)
        self.PF = pgmsface(self.SEQUENCERFACE)
        self.MF = memoryface(self.SEQUENCERFACE)
        self.PROCF = processface(self.SEQUENCERFACE)

        self.ABF.grid(row=0, column=0, columnspan=2)
        self.DF.grid(row=1, column=0)
        self.DBF.grid(row=1, column=1)
        self.PF.grid(row=2, column=0)
        self.MF.grid(row=2, column=1)
        self.PROCF.grid(row=3, column=0, columnspan=2)
        
# Paint Functions ==============================================================

    def paintALU(self):
        v  = self.C.getALUregisters()
        sv = self.ALUF.getALUregisters()
        for i in range(len(v)):
            self.setSVtoV(sv[i], v[i])
        r = self.C.getResult()
        R = self.ALUF.getResult()
        self.setSVtoV(R, r)

    def recolorFunction(self):
        old = self.C.getOldFunction()
        i = 4*old[0] + 2*old[1] + old[2]
        self.ALUF.tagLabels[i].config(fg="black")
        for x in self.ALUF.registerLabels[i]:
            x.config(fg="black")

        new = self.C.getFunction()
        j = 4*new[0] + 2*new[1] + new[2]
        self.ALUF.tagLabels[j].config(fg="red")
        for y in self.ALUF.registerLabels[j]:
            y.config(fg="red")
        # A pair of dictionaries in ALUF would make 
        # this considerably less of a hack. Works.

    def paintFunction(self):
        v  = self.C.getFunction()
        sv = self.FF.getFunction()
        self.setSVtoV(sv, v)
        self.recolorFunction()

    def paintStates(self):
        v = self.C.getCYZS()
        sv = self.SF.getCYZS()
        self.setSVtoV(sv, v)

    def paintDataBus(self):
        v = self.C.getDataBus()
        sv = self.DBF.getDataBus()
        self.setSVtoV(sv, v)

    def paintAddressBus(self):
        v = self.C.getAddressBus()
        sv = self.ABF.getAddressBus()
        self.setSVtoV(sv, v)

    def paintRegister(self):
        v = self.C.getRegisters()
        sv = self.RF.getRegisters()
        for i in range(len(v)):
            self.setSVtoV(sv[i], v[i])

    def paintControl(self):
        v = self.C.getControlRegisters()
        sv = self.CF.getRegisters()
        for i in range(len(v)):
            self.setSVtoV(sv[i], v[i])
        I = self.C.getInstruction()
        Iv = self.CF.getInstruction()
        self.setSVtoV(Iv, I)
        
    def paintMemory(self):
        v = self.C.MEMORY.readMemory()
        sv = self.MF.readMemory()
        self.setSVtoV(sv, v)

    def paintNoPause(self):        
        c = "red" if self.C.NOSTEP == True else "black"
        self.DF.noStepButton.config(fg=c)

    def paintClock(self):
        self.C.updateUpTime()
        self.RF.CLKface.Hsv.set(self.C.H)
        self.RF.CLKface.Msv.set(self.C.M)
        self.RF.CLKface.Ssv.set(self.C.S)

    def paintText(self, t):
        self.PROCF.addText(t)
        sleep(0.03)

    def paintALL(self):
        self.paintALU()
        self.paintFunction()
        self.paintStates()
        self.paintDataBus()
        self.paintAddressBus()
        self.paintRegister()
        self.paintControl()
        self.paintMemory()
        self.paintNoPause()

# Make Buttons =================================================================

    def mkFunctionButtons(self):
        fb = self.FF.FUNCTIONbuttons
        for x in range(len(fb)):
            c = lambda i = x : self.C.updateFunction(i)
            fb[x].config(command = c)

    def mkDataBusButtons(self):
        db = self.DBF.DBbuttons
        for x in range(len(db)):
            c = lambda i = x : self.C.updateDataBus(i)
            db[x].config(command = c)

    def mkAddressBusButtons(self):
        ab = self.ABF.ABbuttons
        for x in range(len(ab)):
            c = lambda i = x : self.C.updateAddressBus(i)
            ab[x].config(command = c)

# Load Buttons =================================================================

    def mkLoadButtons(self):
        self.RF.AloadButton.config(command  = self.C.loadA)
        self.RF.BloadButton.config(command  = self.C.loadB)
        self.RF.CloadButton.config(command  = self.C.loadC)
        self.RF.DloadButton.config(command  = self.C.loadD)
        self.RF.M1loadButton.config(command = self.C.loadM1)
        self.RF.M2loadButton.config(command = self.C.loadM2)
        self.RF.XloadButton.config(command  = self.C.loadX)
        self.RF.YloadButton.config(command  = self.C.loadY)
        self.RF.XYloadButton.config(command = self.C.loadXY)
        
        self.CF.J1loadButton.config(command   = self.C.loadJ1)
        self.CF.J2loadButton.config(command   = self.C.loadJ2)        
        self.CF.INSTloadButton.config(command = self.C.loadInst)
        self.CF.INCloadButton.config(command  = self.C.loadINC)
        self.CF.PCloadButton.config(command   = self.C.loadPC)

        self.MF.READ.config(command = self.C.memRead)

# Select Buttons ===============================================================

    def mkSelectButtons(self):
        self.ALUF.LOADbutton.config(command = self.C.selectResult)
        self.RF.AselectButton.config(command = self.C.selectA)
        self.RF.BselectButton.config(command = self.C.selectB)
        self.RF.CselectButton.config(command = self.C.selectC)
        self.RF.DselectButton.config(command = self.C.selectD)        
        self.RF.M1selectButton.config(command = self.C.selectM1)
        self.RF.M2selectButton.config(command = self.C.selectM2)
        self.RF.XselectButton.config(command = self.C.selectX)
        self.RF.YselectButton.config(command = self.C.selectY)        
        self.RF.MselectButton.config(command = self.C.selectM)
        self.RF.XYselectButton.config(command = self.C.selectXY)

        self.CF.JselectButton.config(command = self.C.selectJ)
        self.CF.PCselectButton.config(command = self.C.selectPC)
        self.CF.INCselectButton.config(command = self.C.selectINC)

        self.MF.WRITE.config(command = self.C.memWrite)

# Run Buttons ==================================================================


    def mkRunButtons(self):
        self.DF.runButton.config(command = self.C.run)
        self.DF.stepButton.config(command = self.C.step)
        self.DF.noStepButton.config(command = self.C.noStep)

        self.PF.button.config(command = \
                lambda : self.C.loadPGM(pgms.testDictionary, self.PF.var))

        self.MF.CLEAR.config(command = self.C.memClear)
        self.MF.RANDOM.config(command = self.C.memRandom)

        self.EF.codeButton.config(command = self.parse)

# Run Buttons ==================================================================

    def parse(self):
        I = self.EF.INSTRUCTION.get()
        self.C.ENCODER.setCode(I)
        self.C.ENCODER.parse()

        if self.C.ENCODER.eval == True:
            self.EF.eval.set(str(self.C.ENCODER.INSTRUCTION))
        else:
            self.EF.eval.set("> INVALID <")

# Initialization ===============================================================

    def __init__(self):
        self.mkConstants()

        self.C = core(self.paintALL)

        self.VH = Tk()
        self.VH.withdraw()

        self.mkTopFaces(self.VH)
        self.mkFunctionButtons()
        self.mkDataBusButtons()
        self.mkAddressBusButtons()
        self.mkLoadButtons()
        self.mkSelectButtons()
        self.mkRunButtons()        
        self.paintALL()
        
        self.C.setClockCallback(self.paintClock)
        self.C.runClockThread()

        self.C.setTextCallback(self.paintText)

        self.VH.mainloop()

if __name__ == '__main__':
    vh = VirtualHarry()

