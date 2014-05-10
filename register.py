#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from sys import exit


class register:
# Support ======================================================================

    def mvAtoZ(self, A, Z):
        if len(A) != len(Z):
            exit("Error 1 in register.py")
        for i in range(len(A)):
            Z[i] = A[i]

# set and get ==================================================================

    def loadA(self, db):
        self.mvAtoZ(db, self.A)

    def loadB(self, db):
        self.mvAtoZ(db, self.B)
        
    def loadC(self, db):
        self.mvAtoZ(db, self.C)
        
    def loadD(self, db):
        self.mvAtoZ(db, self.D)
        
    def loadM1(self, db):
        self.mvAtoZ(db, self.M1)
        
    def loadM2(self, db):
        self.mvAtoZ(db, self.M2)
        
    def loadX(self, db):
        self.mvAtoZ(db, self.X)
        
    def loadY(self, db):
        self.mvAtoZ(db, self.Y)                                                

    def loadXY(self, ab):
        self.mvAtoZ(ab[:8], self.X)
        self.mvAtoZ(ab[8:], self.Y)

# initialization ===============================================================

    def __init__(self):

        self.A  = [0,0,0,0,0,0,0,0]
        self.B  = [0,0,0,0,0,0,0,0]
        self.C  = [0,0,0,0,0,0,0,0]
        self.D  = [0,0,0,0,0,0,0,0]
        self.M1 = [0,0,0,0,0,0,0,0]
        self.M2 = [0,0,0,0,0,0,0,0]
        self.X  = [0,0,0,0,0,0,0,0]
        self.Y  = [0,0,0,0,0,0,0,0]

        self.REGISTERS = [self.A, self.B, self.C, self.D, \
                          self.M1, self.M2, self.X, self.Y]

