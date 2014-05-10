#!/usr/bin/python2.7

# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.

from copy import copy


class alu():
# ===== Support ================================================================

    def mvAtoZ(self, A, Z):
        for i in range(len(Z)):
            Z[i] = A[i]

    def printALU(self):
        f = self.FUNCTION
        Sadd = "* " if f == [0,0,0] else "  "
        Sinc = "* " if f == [0,0,1] else "  "
        Sand = "* " if f == [0,1,0] else "  "
        Sor  = "* " if f == [0,1,1] else "  "
        Sxor = "* " if f == [1,0,0] else "  "
        Snot = "* " if f == [1,0,1] else "  "
        Sshl = "* " if f == [1,1,0] else "  "
        Sclr = "* " if f == [1,1,1] else "  "
        print "            B  " + str(self.B)
        print "            C  " + str(self.C)
        print "       --------------------------------"
        print "       RESULT  " + str(self.RESULT)
        print "======================================="
        print "     FUNCTION  " + str(self.FUNCTION)
        print " old FUNCTION  " + str(self.oldFUNCTION)
        print "======================================="
        print "          ADD" + Sadd + str(self.ADD)
        print "          INC" + Sinc + str(self.INC)
        print "          AND" + Sand + str(self.AND)
        print "           OR" + Sor  + str(self.OR)
        print "          XOR" + Sxor + str(self.XOR)
        print "          NOT" + Snot + str(self.NOT)
        print "          SHL" + Sshl + str(self.SHL)
        print "          CLR" + Sclr + str(self.CLR)
        print "======================================="
        print "        CARRY  " + str(self.CARRY)
        print "         ZERO  " + str(self.ZERO)
        print "         SIGN  " + str(self.SIGN)

# ===== sets ===================================================================

    def setB(self, x):
        self.mvAtoZ(x, self.B)
        self.updateALU()

    def setC(self, x):
        self.mvAtoZ(x, self.C)
        self.updateALU()

    def setFUNCTION(self, f):
        self.mvAtoZ(self.FUNCTION, self.oldFUNCTION)
        self.mvAtoZ(f, self.FUNCTION)
        self.updateALU()

    def updateFUNCTION(self, i):
        self.mvAtoZ(self.FUNCTION, self.oldFUNCTION)
        self.FUNCTION[i] = (0 if self.FUNCTION[i] == 1 else 1)
        self.updateALU()

    def setF0(self, i):
        self.mvAtoZ(self.FUNCTION, self.oldFUNCTION)
        self.FUNCTION[0] = i
        self.updateALU()

    def setF1(self, i):
        self.mvAtoZ(self.FUNCTION, self.oldFUNCTION)
        self.FUNCTION[1] = i
        self.updateALU()

    def setF2(self, i):
        self.mvAtoZ(self.FUNCTION, self.oldFUNCTION)
        self.FUNCTION[2] = i
        self.updateALU()

# ===== Mathematics ============================================================

    def getSum(self, k, b, c):
        return int(((not k) and (not b) and c) or \
                ((not k) and b and (not c)) or \
                (k and (not b) and (not c)) or \
                (k and b and c))

    def getCarry(self, k, b, c):
        return int(((not k) and b and c ) or \
                (k and (not b) and c) or \
                (k and b and (not c)) or \
                (k and b and c))

    def addBandC(self):
        self.ADDcarry = 0
        for i in self.Egnar:
            b = self.B[i]
            c = self.C[i]
            self.ADD[i] = self.getSum(self.ADDcarry, b, c)
            self.ADDcarry = self.getCarry(self.ADDcarry, b, c)

    def incB(self):
        self.INCcarry = 1
        for i in self.Egnar:
            b = self.B[i]
            self.INC[i] = self.getSum(self.INCcarry, b, 0)
            self.INCcarry = self.getCarry(self.INCcarry, b, 0)

    def shlB(self):
        x = copy(self.B)
        x = x[1:] + [x[0]]
        self.mvAtoZ(x, self.SHL)

# ===== Update =================================================================

    def updateALU(self):
        self.updateFunctions()
        self.updateResult()
        self.updateStates()

    def updateFunctions(self):
        self.addBandC()
        self.incB()
        self.shlB()
        for i in self.Range:
            b = self.B[i]
            c = self.C[i]
            self.AND[i] = int(b and c)
            self.OR[i] = int(b or c)
            self.NOT[i] = (0 if b == 1 else 1)
            self.XOR[i] = int(b ^ c)

    def updateResult(self):
        f = tuple(self.FUNCTION)
        F = self.FUNCTIONmap[f]
        self.mvAtoZ(F, self.RESULT)
        # Sets RESULT relative to current function
        # as mapped in the FUNCTIONmap dictionary.

    def updateStates(self):
        self.setCarryState()
        self.setZeroState()
        self.setSignState()

    def setCarryState(self):
        self.CARRY = int(self.ADDcarry == 1 or self.INCcarry == 1)

    def setZeroState(self):
        self.ZERO = int(self.RESULT == [0,0,0,0,0,0,0,0])

    def setSignState(self):
        self.SIGN = int(self.RESULT[0] == 1)

# ===== Initialization =========================================================

    def __init__(self):
        self.Range = range(8)
        self.Egnar = range(7,-1,-1)
        self.Range3 = range(3)

        self.ADDcarry =  0
        self.INCcarry =  0

        self.CARRY =     0
        self.ZERO =      1
        self.SIGN =      0

        self.B =        [0,0,0,0,0,0,0,0]
        self.C =        [0,0,0,0,0,0,0,0]

        self.FUNCTION = [0,0,0]
        self.oldFUNCTION = [0,0,0]

        self.RESULT =   [0,0,0,0,0,0,0,0]

        self.ADD =      [0,0,0,0,0,0,0,0]
        self.INC =      [0,0,0,0,0,0,0,0]
        self.AND =      [0,0,0,0,0,0,0,0]
        self.OR =       [0,0,0,0,0,0,0,0]
        self.XOR =      [0,0,0,0,0,0,0,0]
        self.NOT =      [0,0,0,0,0,0,0,0]
        self.SHL =      [0,0,0,0,0,0,0,0]
        self.CLR =      [0,0,0,0,0,0,0,0]

        self.ALUregisters = [self.ADD, self.INC, self.AND, self.OR, \
                             self.XOR, self.NOT, self.SHL, self.CLR]

        self.FUNCTIONmap = { (0,0,0) : self.ADD, \
            (0,0,1) : self.INC, \
            (0,1,0) : self.AND, \
            (0,1,1) : self.OR, \
            (1,0,0) : self.XOR, \
            (1,0,1) : self.NOT, \
            (1,1,0) : self.SHL, \
            (1,1,1) : self.CLR }

        self.updateALU()


if __name__ == '__main__':
    ALU = alu()
    run = True
    while run:
        print "***************************************"
        print "0: set b"
        print "1: set c"
        print "2: set function"
        print "3: set f0"
        print "4: set f1"
        print "5: set f2"
        print "6: print alu"
        print "7: exit"
        x = int(raw_input("Choice: "))
        if x == 0:
            B = raw_input("B: ")
            L = [ int(i) for i in list(B) ]
            print L
            ALU.setB(L)
        if x == 1:
            C = raw_input("C: ")
            L = [ int(i) for i in list(C) ]
            print L
            ALU.setC(L)
        if x == 2:
            F = raw_input("F: ")
            L = [ int(i) for i in list(F) ]
            print L
            ALU.setFUNCTION(L)
        if x == 3:
            F0 = int(raw_input("F0: "))
            ALU.setF0(F0)
        if x == 4:
            F1 = int(raw_input("F1: "))
            ALU.setF1(F1)
        if x == 5:
            F2 = int(raw_input("F2: "))
            ALU.setF2(F2)
        if x == 6:
            ALU.printALU()
        if x == 7:
            run = False
    print "Exiting alu...."
