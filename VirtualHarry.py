#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from Tkinter import Tk, Toplevel
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
        self.COREFACE     = Toplevel(r)
        self.REGISTERFACE = Toplevel(r)
        self.CONTROLFACE  = Toplevel(r)
        self.FIVEFACE     = Toplevel(r)

        self.COREFACE.geometry("+80+40")
        self.REGISTERFACE.geometry("+280+40")
        self.CONTROLFACE.geometry("+410+325")
        self.FIVEFACE.geometry("+740+40")

        self.ALUF = aluface(self.COREFACE)
        self.FF = functionface(self.COREFACE)
        self.SF = statesface(self.COREFACE)

        self.RF = registerface(self.REGISTERFACE)
        self.CF = controlface(self.CONTROLFACE)

        self.ABF = addressbusface(self.FIVEFACE)
        self.DBF = databusface(self.FIVEFACE)
        self.MF = memoryface(self.FIVEFACE)
        self.DF = decoderface(self.FIVEFACE)
        self.PF = pgmsface(self.FIVEFACE)

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
        # self.paintClock()

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

        self.VH.mainloop()

if __name__ == '__main__':
    vh = VirtualHarry()

