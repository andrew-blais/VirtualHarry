#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


class control:
# Support ======================================================================

    def printRegister(self):
        print "====================================="
        print " J1        = " + str(self.J1)
        print " J2        = " + str(self.J2)
        print " PC1       = " + str(self.PC1)
        print " PC2       = " + str(self.PC2)
        print " IncrUnit1 = " + str(self.IncrUnit1)
        print " IncrUnit1 = " + str(self.IncrUnit2)
        print " Inc1      = " + str(self.INC1)
        print " Inc2      = " + str(self.INC2)
        print "====================================="
        print " Inst      = " + str(self.Inst)


    def mvAtoZ(self, A, Z):
        for i in range(len(A)):
            Z[i] = A[i]
            
    def loadJ1(self, db):
        self.mvAtoZ(db, self.J1)

    def loadJ2(self, db):
        self.mvAtoZ(db, self.J2)
        
    def loadInst(self, db):
        self.mvAtoZ(db, self.Inst)

    def loadINC(self):
        self.mvAtoZ(self.IncrUnit1, self.INC1)
        self.mvAtoZ(self.IncrUnit2, self.INC2)

    def loadPC(self, ab):
        self.mvAtoZ(ab[:8], self.PC1)
        self.mvAtoZ(ab[8:], self.PC2)

    def updateIncrUnit(self, ab):
        U = self.increment(ab)
        self.mvAtoZ(U[:8], self.IncrUnit1)
        self.mvAtoZ(U[8:], self.IncrUnit2)

    def increment(self, i):
        R = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        k = 1
        for x in range(15,-1,-1):
            R[x] = self.getSum(k, i[x], 0)
            k = self.getCarry(k, i[x], 0)
        return R
    
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
    
# initialization ===============================================================

    def __init__(self):

        self.J1        = [0,0,0,0,0,0,0,0]
        self.J2        = [0,0,0,0,0,0,0,0]
        self.PC1       = [0,0,0,0,0,0,0,0]
        self.PC2       = [0,0,0,0,0,0,0,0]
        self.IncrUnit1 = [0,0,0,0,0,0,0,0]
        self.IncrUnit2 = [0,0,0,0,0,0,0,1]
        self.INC1      = [0,0,0,0,0,0,0,0]
        self.INC2      = [0,0,0,0,0,0,0,0]

        self.Inst      = [0,0,0,0,0,0,0,0]
        
        self.REGISTERS = [self.J1, self.J2, self.PC1, self.PC2, \
                          self.IncrUnit1, self.IncrUnit2, self.INC1, self.INC2 ]

