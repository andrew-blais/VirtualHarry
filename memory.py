#!/usr/self.bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from itertools import product


class memory:
# ===== Support ================================================================

    def mvAtoZ(self, A, Z):
        for i in range(len(A)):
            Z[i] = A[i]

    def mkMemory(self):
        b = [0,1]
        MA = list(product(b, b, b, b, \
                          b, b, b, b, \
                          b, b, b, b, \
                          b, b, b))
        R = {}
        for i in MA:
            R.update({i : [0,0,0,0,0,0,0,0]})
        return R

    def setAdress(self, x):
        self.ADDRESS = tuple(x[1:])
        # Memory addresses are 15 bits, but the address
        # bus is 16 bits. So, the highest bit is dropped.

    def readMemory(self):
        return self.M[self.ADDRESS]

    def writeMemory(self, x):
        self.mvAtoZ(x, self.M[self.ADDRESS])

# ===== Initialization =========================================================

    def __init__(self):
        self.M = self.mkMemory()
        
        self.ADDRESS = (0, 0, 0, 0, \
                        0, 0, 0, 0, \
                        0, 0, 0, 0, \
                        0, 0, 0)

# ===== Test ===================================================================

#if __name__ == '__main__':
#    m = memory()



