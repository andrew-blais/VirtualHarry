

testGOTOpgm = [ \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,1,0,0,1,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], [0,0,1,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], [1,0,1,0,1,1,1,0]) \
     ]

testSETMpgm = [ \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,0,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,1,1,0,0,1,1,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], [1,1,1,1,1,1,1,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], [1,0,1,0,1,1,1,0])  \
     ]

testLOADpgm = [ \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,0,0,1,0,0,1,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,1,0,1,1,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], [1,1,1,1,1,1,1,1])  \
     ]

testSETABpgm = [ \
      ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,1,0,0,0,1,1,1]), \
      ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,1,0,1,1,1,0])  \
      ]

subtractPGM = [ \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,0,0,0,0,1,0,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,1,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], [1,0,0,0,0,0,0,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], [0,0,0,0,1,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], [1,0,0,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1], [1,0,1,0,1,1,1,0])  \
     ]

multiplyPGM = [ \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,1,0,1,1,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [0,1,0,1,1,0,0,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], [0,0,0,1,1,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], [0,1,1,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], [0,0,0,1,0,1,1,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1], [1,0,0,0,0,0,1,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0], [1,1,1,1,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1], [0,0,0,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], [0,0,0,0,1,0,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1], [0,0,1,0,1,0,0,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0], [0,0,0,0,1,1,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1], [1,0,0,0,0,1,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0], [0,0,0,1,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1], [0,1,1,1,1,1,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0], [1,0,0,0,0,0,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1], [0,0,1,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0], [0,0,0,0,1,1,0,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1], [1,0,0,0,0,1,0,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0], [1,1,1,1,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1], [0,0,0,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0], [0,0,0,1,1,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1], [0,0,0,0,1,1,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0], [1,0,0,0,0,0,0,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1], [0,0,1,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0], [0,0,0,0,1,1,0,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1], [1,0,0,0,0,1,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0], [0,0,0,1,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1], [0,1,1,1,1,1,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0], [1,0,0,0,0,0,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1], [0,0,1,0,1,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0], [0,0,0,0,1,1,1,1]), \
     ([0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1], [1,0,0,0,0,1,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], [0,0,1,1,1,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1], [0,0,0,0,1,1,1,1]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0], [1,0,0,0,0,1,0,1]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1], [1,1,1,1,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0], [0,0,0,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1], [0,0,1,1,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0], [0,0,0,0,1,1,0,1]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1], [0,0,0,1,0,1,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0], [1,0,0,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1], [0,0,1,0,1,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0], [1,1,1,0,1,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1], [0,0,0,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0], [0,0,1,1,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1], [0,0,0,0,1,1,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0], [1,0,0,0,0,0,0,1]), \
     ([0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1], [0,0,1,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0], [0,0,0,0,1,0,1,1]), \
     ([0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1], [1,0,0,0,1,0,0,1]), \
     ([0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0], [1,1,1,0,0,0,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1], [0,0,0,0,0,0,0,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0], [0,0,0,0,1,0,1,0]), \
     ([0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1], [1,0,1,0,1,1,1,0])  \
     ]
