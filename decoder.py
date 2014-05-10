#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from random import randint
from itertools import product


class decoder:
# Support ======================================================================
    
    def mvAtoZ(self, A, Z):
        for i in range(len(A)):
            Z[i] = A[i]
    
    def randomInstruction(self):
        self.mvAtoZ([ randint(0,1) for unused_i in range(8)], self.Inst)

    def mkAllInstructions(self):
        b = [0,1]
        self.allInstructions = list(product(b,b,b,b,b,b,b,b))
        
    def setInstruction(self, x):
        self.mvAtoZ(x, self.Inst)

# Decode =======================================================================

    def MOV(self):
        D = self.registerMap[tuple(self.Inst[2:5])]
        S = self.registerMap[tuple(self.Inst[5:8])]
        print "Select " + S 
        print "Load " + D

    def SETAB(self):
        if self.Inst[2] == 0:
            print "SET A to " + str(self.Inst[3:8])
        else:
            print "SET B to " + str(self.Inst[3:8])

    def ALU(self):
        print "SET ALU FUNCTION to " + str(self.Inst[5:8])
        if self.Inst[4] == 0:
            print "Stored result in A"
        else:
            print "Stored result in D"

    def LOAD(self):
        if self.Inst[6:8] == [0,0]:
            print "LOAD MEMORY to A"
        else:
            if self.Inst[6:8] == [0,1]:
                print "LOAD MEMORY to B"
            else:
                if self.Inst[6:8] == [1,0]:
                    print "LOAD MEMORY to C"
                else:
                    print "LOAD MEMORY to D"

    def STORE(self):
        if self.Inst[6:8] == [0,0]:
            print "STORE A in MEMORY"
        else:
            if self.Inst[6:8] == [0,1]:
                print "STORE B in MEMORY"
            else:
                if self.Inst[6:8] == [1,0]:
                    print "STORE C in MEMORY"
                else:
                    print "STORE D in MEMORY"

    def RET_MOV16(self):
        if self.Inst[5:7] == [1,1]:
            print "RET...HALT"
        else:
            d = "XY" if self.Inst[4] == 0 else "PC"
            s = ""
            s = s + ("M" if self.Inst[5:7] == [0,0] else "")
            s = s + ("XY" if self.Inst[5:7] == [0,1] else "")
            s = s + ("J" if self.Inst[5:7] == [1,0] else "")
            print "MOV16 " + s + " to " + d 

    def INC(self):
        print "INC: set XY to XY + 1"
    
    def SETM(self):
        print "SETM: Move next 16 bits to M"
    
    def GOTO(self):
        print "GOTO: set address bus to next 16 bits"

    def CALL(self):
        print "CALL: Move PC to XY"
        
    def BC(self):
        print "BC"

    def execute(self):
        if self.Inst[0] == 0:
            if self.Inst[1] == 0:
                self.MOV()
            else:
                self.SETAB()
        else:
            if self.Inst[1] == 0:
                if self.Inst[2] == 0:
                    if self.Inst[3] == 0:
                        self.ALU()
                    else:
                        if self.Inst[4] == 0:
                            self.LOAD()
                        else:
                            self.STORE()
                else:
                    if self.Inst[3] == 0:
                        self.RET_MOV16()
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

    def decodeAll(self):
        for i in self.allInstructions:
            self.setInstruction(i)
            print self.Inst
            self.execute()
            print "==========================="

    def decodeRandom(self):
        self.randomInstruction()
        self.execute()
        print "==========================="

# ===== Initialization =========================================================

    def __init__(self):
        self.Inst = [0,0,0,0,0,0,0,0]

        self.mkAllInstructions()
        
        self.registerMap = { (0,0,0) : "A", \
                            (0,0,1) : "B", \
                            (0,1,0) : "C", \
                            (0,1,1) : "D", \
                            (1,0,0) : "M1", \
                            (1,0,1) : "M2", \
                            (1,1,0) : "X", \
                            (1,1,1) : "Y" }










# ==============================================================================