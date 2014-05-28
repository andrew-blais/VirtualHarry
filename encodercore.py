#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the
# GNU General Public License version 3.


class encodercore:

    def parse(self):
        self.evaluation = True
        S = self.code.split()

        if S[0] in self.operationDICT.keys():
            self.operationDICT[S[0]]()
        else:
            self.evaluation = False
            self.TextCallback("PARSE ERROR: first element error")
            
        if self.evaluation == True:
            self.TextCallback(self.code)
            self.TextCallback("code: " + str(self.INSTRUCTION))

    def MOV8(self):
        #self.TextCallback("MOV8")
        self.INSTRUCTION = [0,0]
        S = self.code.split()

        if len(S) != 3:
            self.evaluation = False
            self.TextCallback("MOV8 ERROR: wrong number of elements")
        else:
            if S[1] in self.abcdm1m2xyDICT.keys():
                self.INSTRUCTION = self.INSTRUCTION + self.abcdm1m2xyDICT[S[1]]
            else:
                self.evaluation = False
                self.TextCallback("MOV8 ERROR: second element error")
            if S[2] in self.abcdm1m2xyDICT.keys():
                self.INSTRUCTION = self.INSTRUCTION + self.abcdm1m2xyDICT[S[2]]
            else:
                self.evaluation = False
                self.TextCallback("MOV8 ERROR: third element error")

    def SETAB(self):
        #self.TextCallback("SETAB")
        self.INSTRUCTION = [0,1]
        S = self.code.split()

        if len(S) != 3:
            self.evaluation = False
            self.TextCallback("SETAB ERROR: wrong number of elements")
        else:
            if S[1] in self.abDICT.keys():
                self.INSTRUCTION = self.INSTRUCTION + self.abDICT[S[1]]
                if self.checkForm(S[2], 5) == True:
                    self.INSTRUCTION = self.INSTRUCTION +  self.mkList(S[2])
                else:
                    self.evaluation = False
                    self.TextCallback("SETAB ERROR: third element error")
            else:
                self.evaluation = False
                self.TextCallback("SETAB ERROR: second element error")

    def ALU(self):
        #self.TextCallback("ALU")
        self.INSTRUCTION = [1,0,0,0]
        S = self.code.split()

        if len(S) != 3:
            self.evaluation = False
            self.TextCallback("ALU ERROR: wrong number of elements")
        else:
            if S[1] in self.adDICT.keys():
                self.INSTRUCTION = self.INSTRUCTION + self.adDICT[S[1]]
                if S[2] in self.functionDICT.keys():
                    self.INSTRUCTION = self.INSTRUCTION + self.functionDICT[S[2]]
                else:
                    self.evaluation = False
                    self.TextCallback("ALU ERROR: third element error")
            else:
                self.evaluation = False
                self.TextCallback("ALU ERROR: second element error")

    def LOAD(self):
        #self.TextCallback("LOAD")
        self.INSTRUCTION = [1,0,0,1,0,0]
        S = self.code.split()

        if len(S) != 2:
            self.evaluation = False
            self.TextCallback("LOAD ERROR: wrong number of elements")
        else:
            if S[1] in self.abcdDICT.keys():
                self.INSTRUCTION = self.INSTRUCTION + self.abcdDICT[S[1]]
            else:
                self.evaluation = False
                self.TextCallback("LOAD ERROR: second element error")

    def STORE(self):
        #self.TextCallback("STORE")
        self.INSTRUCTION = [1,0,0,1,1,0]
        S = self.code.split()

        if len(S) != 2:
            self.evaluation = False
            self.TextCallback("STORE ERROR: wrong number of elements")
        else:
            if S[1] in self.abcdDICT.keys():
                self.INSTRUCTION = self.INSTRUCTION + self.abcdDICT[S[1]]
            else:
                self.evaluation = False
                self.TextCallback("STORE ERROR: second element error")

    def RET(self):
        #self.TextCallback("RET")
        S = self.code.split()
        if len(S) != 1:
            self.evaluation = False
            self.TextCallback("RET ERROR: wrong number of elements")
        else:
            self.INSTRUCTION = [1,0,1,0,1,1,1,0]

    def MOV16(self):
        #self.TextCallback("MOV16")
        self.INSTRUCTION = [1,0,1,0]
        S = self.code.split()

        if len(S) != 3:
            self.evaluation = False
            self.TextCallback("MOV16 ERROR: wrong number of elements")
        else:
            if S[1] in self.xypcDICT.keys():
                self.INSTRUCTION = self.INSTRUCTION + self.xypcDICT[S[1]]
                if S[2] in self.mxyjDICT.keys():
                    self.INSTRUCTION = self.INSTRUCTION + self.mxyjDICT[S[2]]
                else:
                    self.evaluation = False
                    self.TextCallback("MOV16 ERROR: third element error")
            else:
                self.evaluation = False
                self.TextCallback("MOV16 ERROR: second element error")

        self.INSTRUCTION = self.INSTRUCTION + [0]

    def INC(self):
        #self.TextCallback("INC")
        self.INSTRUCTION = [1,0,1,1,0,0,0,0]

    def checkForm(self, x, n):
        R = True
        if len(x) != n:
            R = False
        for i in x:
            if i not in ["0", "1"]:
                R = False
        return R

    def mkList(self, x):
        return [ int(i) for i in x ]

    def GOTO(self):
        #self.TextCallback("GOTO")
        self.INSTRUCTION = [1,1,1,0,0,1,1,0]
        S = self.code.split()

        if len(S) != 3:
            self.evaluation = False
            self.TextCallback("GOTO ERROR: wrong number of elements")
        else:
            if self.checkForm(S[1], 8) == True:
                self.ADDRESS1 = self.mkList(S[1])
                if self.checkForm(S[2], 8) == True:
                    self.ADDRESS2 = self.mkList(S[2])
                else:
                    self.evaluation = False
                    self.TextCallback("GOTO ERROR: third element error")
            else:
                self.evaluation = False
                self.TextCallback("GOTO ERROR: second element error")

    def SETM(self):
        #self.TextCallback("SETM")
        self.INSTRUCTION = [1,1,0,0,0,0,0,0]
        S = self.code.split()

        if len(S) != 3:
            self.evaluation = False
            self.TextCallback("SETM ERROR: wrong number of elements")
        else:
            if self.checkForm(S[1], 8) == True:
                self.ADDRESS1 = self.mkList(S[1])
            else:
                self.evaluation = False
                self.TextCallback("SETM ERROR: second element error")
            if self.checkForm(S[2], 8) == True:
                self.ADDRESS2 = self.mkList(S[2])
            else:
                self.evaluation = False
                self.TextCallback("SETM ERROR: third element error")

    def CALL(self):
        #self.TextCallback("CALL")
        self.INSTRUCTION = [1,1,1,0,0,1,1,1]
        S = self.code.split()

        if len(S) != 3:
            self.evaluation = False
            self.TextCallback("CALL ERROR: wrong number of elements")
        else:
            if self.checkForm(S[1], 8) == True:
                self.ADDRESS1 = self.mkList(S[1])
            else:
                self.evaluation = False
                self.TextCallback("CALL ERROR: second element error")
            if self.checkForm(S[2], 8) == True:
                self.ADDRESS2 = self.mkList(S[2])
            else:
                self.evaluation = False
                self.TextCallback("CALL ERROR: third element error")

    def BC(self):
        #self.TextCallback("BC")
        self.INSTRUCTION = [1,1,1]
        S = self.code.split()

        if len(S) != 7:
            self.evaluation = False
            self.TextCallback("BC ERROR: wrong number of elements")
        else:
            if S[1] in self.signDICT.keys():
                self.INSTRUCTION = self.INSTRUCTION + self.signDICT[S[1]]

                if S[2] in self.carryDICT.keys():
                    self.INSTRUCTION = self.INSTRUCTION + self.carryDICT[S[2]]

                    if S[3] in self.zero1DICT.keys():
                        self.INSTRUCTION = self.INSTRUCTION + self.zero1DICT[S[3]]

                        if S[4] in self.zero0DICT.keys():
                            self.INSTRUCTION = self.INSTRUCTION + self.zero0DICT[S[4]]
                            self.INSTRUCTION = self.INSTRUCTION + [0]

                            if self.checkForm(S[5], 8) == True:
                                self.ADDRESS1 = self.mkList(S[5])

                                if self.checkForm(S[6], 8) == True:
                                    self.ADDRESS2 = self.mkList(S[6])
                                else:
                                    self.evaluation = False
                                    self.TextCallback("BC ERROR: seventh element error")                            
                            else:
                                self.evaluation = False
                                self.TextCallback("BC ERROR: sixth element error")
                        else:
                            self.evaluation = False
                            self.TextCallback("BC ERROR: fifth element error")
                    else:
                        self.evaluation = False
                        self.TextCallback("BC ERROR: fourth element error")
                else:
                    self.evaluation = False
                    self.TextCallback("BC ERROR: third element error")
            else:
                self.evaluation = False
                self.TextCallback("BC ERROR: second element error")

    def setCode(self, x):
        self.code = x
        
    def setTextCallback(self, tcb):
        self.TextCallback = tcb

    def __init__(self):

        self.code = ""
        self.evaluation = True
        self.INSTRUCTION = []
        self.ADDRESS1 = []
        self.ADDRESS2 = []

        self.operationDICT = { \
                     "MOV8" : self.MOV8, \
                     "SETAB" : self.SETAB, \
                     "ALU" : self.ALU, \
                     "LOAD" : self.LOAD, \
                     "STORE" : self.STORE, \
                     "RET" : self.RET, \
                     "MOV16" : self.MOV16, \
                     "INC" : self.INC, \
                     "GOTO" : self.GOTO, \
                     "SETM" : self.SETM, \
                     "CALL" : self.CALL, \
                     "BC" : self.BC \
                     }

        self.abcdm1m2xyDICT = { \
                     "A" : [0,0,0], \
                     "B" : [0,0,1], \
                     "C" : [0,1,0], \
                     "D" : [0,1,1], \
                     "M1" : [1,0,0], \
                     "M2" : [1,0,1], \
                     "X" : [1,1,0], \
                     "Y" : [1,1,1] \
                     }

        self.abDICT = { \
                     "A" : [0], \
                     "B" : [1] \
                     }

        self.abcdDICT = { \
                     "A" : [0,0], \
                     "B" : [0,1], \
                     "C" : [1,0], \
                     "D" : [1,1] \
                     }

        self.xypcDICT = { \
                     "XY" : [0], \
                     "PC" : [1] \
                     }


        self.mxyjDICT = { \
                     "M" : [0,0], \
                     "XY" : [0,1], \
                     "J" : [1,0] \
                     }

        self.functionDICT = { \
                     "ADD" : [0,0,0], \
                     "INC" : [0,0,1], \
                     "AND" : [0,1,0], \
                     "OR"  : [0,1,1], \
                     "XOR" : [1,0,0], \
                     "NOT" : [1,0,1], \
                     "SHL" : [1,1,0], \
                     "CLR" : [1,1,1] \
                     }

        self.adDICT = { \
                     "A" : [0], \
                     "D" : [1] \
                     }

        self.signDICT = {\
                     "S1-" : [0], \
                     "S1+" : [1] \
                     }

        self.carryDICT = {\
                     "Cy0-" : [0], \
                     "Cy0+" : [1] \
                     }

        self.zero1DICT = {\
                     "Z1-" : [0], \
                     "Z1+" : [1] \
                     }

        self.zero0DICT = {\
                     "Z0-" : [0], \
                     "Z0+" : [1] \
                     }
