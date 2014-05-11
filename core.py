#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from alu import alu
from register import register
from control import control
from memory import memory
from thread import start_new_thread
import pgms


class core():
# ===== Support ================================================================

    def mvAtoZ(self, A, Z):
        for i in range(len(A)):
            Z[i] = A[i]

    def StoL(self, s, x):
        R = []
        for i in s:
            R.append(0 if i == "0" else 1)
        if x == 3 and len(s) != 3:
            R = [0,0,0]            
        if x == 8 and len(s) != 8:
            R = [0,0,0,0,0,0,0,0]
        if x == 16 and len(s) != 16:
            R = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        return R

# Decode & Execute =============================================================

    def fetchAndIncrement(self):
        print "<<< FETCH >>>"
        self.selectPC()
        self.memRead()
        self.loadInst()
        print "<<< INCREMENT >>>"
        self.loadINC()
        self.selectINC()
        self.loadPC()

    def MOV(self):
        print "MOVE"
        if self.Inst[2:5] == self.Inst[5:8]:
            self.setDataBus([0,0,0,0,0,0,0,0])
            print "D = S: set to [0,0,0,0,0,0,0,0]"
        else:
            print "Moving stuff: "
            self.regSelectMap[tuple(self.Inst[5:8])]()
        self.regLoadMap[tuple(self.Inst[2:5])]()

    def SETAB(self):
        print "SETAB"
        p = [1,1,1] if self.Inst[3] == 1 else [0,0,0]
        # Since the negative numbers are represented by "two's
        # complement" the first three digits will be either 0s or
        # 1s depending on whether the number is positive, zero or
        # negative. This fixes that. 
        self.setDataBus(p + self.Inst[3:8])
        if self.Inst[2] == 0:
            self.loadA()
        else:
            self.loadB()
        print str(p + self.Inst[3:8])

    def ALUfunction(self):
        print "ALU function: " + str(self.Inst[5:8])
        self.setFunction(self.Inst[5:8])
        self.selectResult()
        if self.Inst[4] == 0:
            self.loadA()
        else:
            self.loadD()

    def LOAD(self):
        print "LOAD"
        self.selectM()
        self.memRead()
        if self.Inst[6:8] == [0,0]:
            self.loadA()
        else:
            if self.Inst[6:8] == [0,1]:
                self.loadB()
            else:
                if self.Inst[6:8] == [1,0]:
                    self.loadC()
                else:
                    self.loadD()

    def STORE(self):
        print "STORE"
        self.selectM()
        if self.Inst[6:8] == [0,0]:
            self.selectA()
        else:
            if self.Inst[6:8] == [0,1]:
                self.selectB()
            else:
                if self.Inst[6:8] == [1,0]:
                    self.selectC()
                else:
                    self.selectD()
        self.memWrite()

    def RET_MOV16(self):
        print  "RETURN / MOVE 16 bits >>> " + str(self.Inst)
        RUN = True
        if self.Inst[5:7] == [1,1]:
            print "HALT "
            # Set PC to zero................................
            self.mvAtoZ([0,0,0,0,0,0,0,0], self.CONTROL.PC1)
            self.mvAtoZ([0,0,0,0,0,0,0,0], self.CONTROL.PC2)
            RUN = False 
        else:
            print "MOV16"
            if self.Inst[4] == 0: # d is XY
                if self.Inst[5:7] == [0,0]:
                    self.selectM()
                    
                if self.Inst[5:7] == [0,1]: # What would Harry's machine do?
                    self.selectXY() 

                if self.Inst[5:7] == [1,0]:
                    self.selectJ()
                self.loadXY()
            else: # d is PC
                if self.Inst[5:7] == [0,0]:
                    self.selectM()
                if self.Inst[5:7] == [0,1]:
                    self.selectXY()
                if self.Inst[5:7] == [1,0]:
                    self.selectJ()
                self.loadPC()
        return RUN

    def INC(self):
        print "INC: XY > XY + 1"
        self.selectXY()
        self.loadINC()
        self.selectINC()
        self.loadXY()

    def SETM(self):
        print "SETM: Move next 16 bits to M"
        self.memRead()
        self.loadM1()
        self.loadINC()
        self.selectINC()
        self.memRead()
        self.loadM2()
        self.loadINC()
        self.selectINC()
        self.loadPC()

    def GOTO(self):
        print "GOTO: set address bus, PC, to next 16 bits"
        self.memRead()
        self.loadJ1()
        self.loadINC()
        self.selectINC()
        self.memRead()
        self.loadJ2()
        self.selectJ()
        self.loadPC()

    def CALL(self):
        print "CALL: set address bus to next 16 bits & PC => XY"
        # CALL is like GOTO except that the address of the next instruction 
        # after CALL is saved in XY.
        self.memRead()
        self.loadJ1()
        self.loadINC()
        self.selectINC()
        self.memRead()
        self.loadJ2()
        self.loadINC()
        self.selectINC()
        self.loadXY()
        self.selectJ()
        self.loadPC()

    def BC(self):
        print "Branch Conditionally"
        C0 = (self.Inst[3] == 1) and (self.ALU.SIGN  == 1) 
        C1 = (self.Inst[4] == 1) and (self.ALU.CARRY == 0)
        C2 = (self.Inst[5] == 1) and (self.ALU.ZERO  == 1)
        C3 = (self.Inst[6] == 1) and (self.ALU.ZERO  == 0)

        if C0 or C1 or C2 or C3:
            self.memRead()
            self.loadJ1()
            self.loadINC()
            self.selectINC()
            self.memRead()
            self.loadJ2()
            self.selectJ()
            self.loadPC()
        else:
            self.loadINC()
            self.selectINC()
            self.loadINC()
            self.selectINC()
            self.loadPC()

    def execute(self):
        print "<<< EXECUTE >>>"
        RUN = True
        if self.Inst[0] == 0:
            if self.Inst[1] == 0:
                self.MOV()
            else:
                self.SETAB()
        else:
            if self.Inst[1] == 0:
                if self.Inst[2] == 0:
                    if self.Inst[3] == 0:
                        self.ALUfunction()
                    else:
                        if self.Inst[4] == 0:
                            self.LOAD()
                        else:
                            self.STORE()
                else:
                    if self.Inst[3] == 0:
                        RUN = self.RET_MOV16()
                    else:
                        self.INC()
            else:
                if self.Inst[2] == 0:
                    self.SETM()
                else:
                    if self.Inst[5:7] == [1,1]:
                        if self.Inst[7] == 0:
                            self.GOTO()
                        else:
                            self.CALL()
                    else:
                        self.BC()
        print "*************************************************"
        return RUN

# ===== RUN & testing ==========================================================

    def step(self):
        self.PAUSE = False

    def pause(self):
        while self.PAUSE == True:
            pass
        self.PAUSE = True
        
    def noStep(self):
        self.NOSTEP = True if self.NOSTEP == False else False
        self.CALLBACK()

    def FetchIncrementExecute(self):
        self.PAUSE = True
        self.RUN = True
        while self.RUN == True:
            self.fetchAndIncrement()
            self.RUN = self.execute()            
            if self.RUN == True and self.NOSTEP == False:
                self.pause() # Time to inspect VH

        print "================================================================"

    def run(self):
        start_new_thread(self.FetchIncrementExecute, ())

# ===== Programs ===============================================================
        
    def loadPGM(self, pgm):
        for i in pgm:
            self.MEMORY.setAdress(i[0])
            self.MEMORY.writeMemory(i[1])
        self.MEMORY.setAdress([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.CALLBACK()

    def testGOTO(self):
        self.loadPGM(pgms.testGOTOpgm)

    def testSETM(self):
        self.loadPGM(pgms.testSETMpgm)

    def testLOAD(self):
        self.loadPGM(pgms.testLOADpgm)
        
    def testSETAB(self):
        self.loadPGM(pgms.testSETABpgm)

    def subtract(self):
        self.loadPGM(pgms.subtractPGM)

    def multiply(self):
        self.loadPGM(pgms.multiplyPGM)

# ===== Initialization =========================================================

    def __init__(self, cb=None):
        self.RANGE   = range(8)
        self.EGNAR   = range(7,-1,-1)
        self.RANGE3  = range(3)
        self.RANGE16 = range(16)
        self.EGNAR16 = range(15,-1,-1)

        self.PAUSE = True
        self.NOSTEP = False
        self.RUN = True

        self.ALU = alu()
        self.REGISTER = register()
        self.CONTROL = control()

        self.DATABUS = [0,0,0,0,0,0,0,0]
        self.ADDRESSBUS = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        self.MEMORY = memory()
        
        self.CALLBACK = cb

        self.CONTROLREGISTER = [0,0,0] # Cy, Z, S
        
        self.Inst = [0,0,0,0,0,0,0,0]

        self.regLoadMap = { (0,0,0) : self.loadA, \
                            (0,0,1) : self.loadB, \
                            (0,1,0) : self.loadC, \
                            (0,1,1) : self.loadD, \
                            (1,0,0) : self.loadM1, \
                            (1,0,1) : self.loadM2, \
                            (1,1,0) : self.loadX, \
                            (1,1,1) : self.loadY }

        self.regSelectMap = { (0,0,0) : self.selectA, \
                              (0,0,1) : self.selectB, \
                              (0,1,0) : self.selectC, \
                              (0,1,1) : self.selectD, \
                              (1,0,0) : self.selectM1, \
                              (1,0,1) : self.selectM2, \
                              (1,1,0) : self.selectX, \
                              (1,1,1) : self.selectY }

# ===== ALU ====================================================================

    def getResult(self):
        return self.ALU.RESULT

    def getCYZS(self):
        return [self.ALU.CARRY, self.ALU.ZERO, self.ALU.SIGN]

    def loadCtrlReg(self):
        self.mvAtoZ(self.getCYZS(), self.CONTROLREGISTER)

    def getOldFunction(self):
        return self.ALU.oldFUNCTION

    def getFunction(self):
        return self.ALU.FUNCTION

    def getALUregisters(self):
        return self.ALU.ALUregisters

    def updateFunction(self, i):
        self.ALU.updateFUNCTION(i)
        self.CALLBACK()

    def setFunction(self, f):
        print "setFunction"
        self.ALU.setFUNCTION(f)
        self.CALLBACK()
        
    def setF0(self, i):
        print "set F0"
        self.ALU.setF0(i)
        self.CALLBACK()

    def setF1(self, i):
        print "set F1"
        self.ALU.setF1(i)
        self.CALLBACK()

    def setF2(self, i):
        print "set F2"        
        self.ALU.setF2(i)
        self.CALLBACK()

    def printALU(self):
        self.ALU.printALU()

# ===== Register ===============================================================

    def getRegisters(self):
        return self.REGISTER.REGISTERS

    def printRegister(self):
        self.REGISTER.printRegister()

# ===== Data bus ===============================================================

    def updateDataBus(self, i):
        self.DATABUS[i] = 0 if self.DATABUS[i] == 1 else 1
        self.CALLBACK()

    def setDataBus(self, x):
        self.mvAtoZ(x, self.DATABUS)
        self.CALLBACK()

    def getDataBus(self):
        return self.DATABUS

    def printDataBus(self):
        print "data bus: " + str(self.getDataBus())

# ===== Register Load ==========================================================

    def loadA(self):
        print "loadA"
        self.REGISTER.loadA(self.DATABUS)
        self.CALLBACK()

    def loadB(self):
        print "loadB"
        self.REGISTER.loadB(self.DATABUS)
        self.ALU.setB(self.DATABUS)
        self.CALLBACK()
            
    def loadC(self):
        print "loadC"
        self.REGISTER.loadC(self.DATABUS)
        self.ALU.setC(self.DATABUS)
        self.CALLBACK()
            
    def loadD(self):
        print "loadD"
        self.REGISTER.loadD(self.DATABUS)
        self.CALLBACK()
            
    def loadM1(self):
        print "loadM1"
        self.REGISTER.loadM1(self.DATABUS)
        self.CALLBACK()
            
    def loadM2(self):
        print "loadM2"
        self.REGISTER.loadM2(self.DATABUS)
        self.CALLBACK()
                    
    def loadX(self):
        print "loadX"
        self.REGISTER.loadX(self.DATABUS)
        self.CALLBACK()

    def loadY(self):
        print "loadY"
        self.REGISTER.loadY(self.DATABUS)
        self.CALLBACK()

    def loadXY(self):
        print "loadXY"
        self.REGISTER.loadXY(self.ADDRESSBUS)
        self.CALLBACK()

# ===== Control Load ===========================================================

    def loadJ1(self):
        print "load j1"
        self.CONTROL.loadJ1(self.DATABUS)
        self.CALLBACK()

    def loadJ2(self):
        print "load j2"
        self.CONTROL.loadJ2(self.DATABUS)
        self.CALLBACK()

    def loadInst(self):
        self.CONTROL.loadInst(self.DATABUS)
        self.mvAtoZ(self.DATABUS, self.Inst)
        print "load Inst: " + str(self.Inst)
        self.CALLBACK()

    def loadINC(self):
        print "loadINC"
        self.CONTROL.loadINC()
        self.CALLBACK()

    def loadPC(self):
        print "loadPC"
        self.CONTROL.loadPC(self.ADDRESSBUS)
        self.CALLBACK()

# ===== Register Select ========================================================

    def selectA(self):
        print "selectA"
        self.mvAtoZ(self.REGISTER.A, self.DATABUS)
        self.CALLBACK()
            
    def selectB(self):
        print "selectB"
        self.mvAtoZ(self.REGISTER.B, self.DATABUS)
        self.CALLBACK()
        
    def selectC(self):
        print "selectC"
        self.mvAtoZ(self.REGISTER.C, self.DATABUS)
        self.CALLBACK()

    def selectD(self):
        print "selectD"
        self.mvAtoZ(self.REGISTER.D, self.DATABUS)
        self.CALLBACK()
            
    def selectM1(self):
        print "selectM1"
        self.mvAtoZ(self.REGISTER.M1, self.DATABUS)
        self.CALLBACK()
        
    def selectM2(self):
        print "selectM2"
        self.mvAtoZ(self.REGISTER.M2, self.DATABUS)
        self.CALLBACK()
                    
    def selectX(self):
        print "selectX"
        self.mvAtoZ(self.REGISTER.X, self.DATABUS)
        self.CALLBACK()

    def selectY(self):
        print "selectY"
        self.mvAtoZ(self.REGISTER.Y, self.DATABUS)
        self.CALLBACK()
            
    def mvToAddressBus(self, R1, R2):
        for i in self.RANGE16:
            if i < 8:
                self.ADDRESSBUS[i] = R1[i]
            else:
                self.ADDRESSBUS[i] = R2[i - 8]
        self.updateIncrUnit()
        self.addressBusToMemory()
        self.CALLBACK()

    def selectM(self):
        print "selectM"
        self.mvToAddressBus(self.REGISTER.M1, self.REGISTER.M2)

    def selectXY(self):
        print "selectXY"
        self.mvToAddressBus(self.REGISTER.X, self.REGISTER.Y)

# ==============================================================================            
            
    def selectResult(self):
        print "selectRESULT"
        self.mvAtoZ(self.ALU.RESULT, self.DATABUS)
        self.CALLBACK()

# ==============================================================================

    def selectJ(self):
        print "selectJ"
        self.mvToAddressBus(self.CONTROL.J1, self.CONTROL.J2)

    def selectPC(self):
        print "selectPC"
        self.mvToAddressBus(self.CONTROL.PC1, self.CONTROL.PC2)

    def selectINC(self):
        print "selectINC"
        self.mvToAddressBus(self.CONTROL.INC1, self.CONTROL.INC2)

# ===== Addressbus =============================================================

    def updateAddressBus(self, i):
        self.ADDRESSBUS[i] = 0 if self.ADDRESSBUS[i] == 1 else 1
        self.updateIncrUnit()
        self.addressBusToMemory()
        self.CALLBACK()

    def setAddressBus(self, x):
        self.mvAtoZ(x, self.ADDRESSBUS)
        self.updateIncrUnit()
        self.addressBusToMemory()
        self.CALLBACK()

    def getAddressBus(self):
        return self.ADDRESSBUS

    def printAddressBus(self):
        print "address bus: " + str(self.ADDRESSBUS)

# ===== Control ================================================================

    def updateIncrUnit(self):
        self.CONTROL.updateIncrUnit(self.ADDRESSBUS)

    def getInstruction(self):
        return self.CONTROL.Inst

    def getControlRegisters(self):
        return self.CONTROL.REGISTERS

    def printControl(self):
        self.CONTROL.printRegister()

# ===== Memory =================================================================

    def addressBusToMemory(self):
        self.MEMORY.setAdress(self.ADDRESSBUS)
        self.CALLBACK()

    def memRead(self):
        print "memRead"
        self.mvAtoZ(self.MEMORY.readMemory(), self.DATABUS)
        self.CALLBACK()

    def memWrite(self):
        print "memWrite"
        self.MEMORY.writeMemory(self.DATABUS)
        self.CALLBACK()

# ==============================================================================




