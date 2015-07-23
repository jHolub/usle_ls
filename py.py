from __future__ import division
from pylab import *

import numpy as np
import time
import math

Z = np.array([
            [9,8,6,5,4],
            [9,8,6,5,4],
            [9,7,6,4,3],
            [9,7,6,4,3]
            ])
#    Z2    Z6    Z3
#    Z8    Z     Z7
#    Z4    Z5    Z1

Z = np.arange(100000000.0).reshape(10000,10000) 
           
rows,cols = len(Z), len(Z[0])

#zz = np.empty(shape=(rows-2,cols-2), dtype=float)
zz = Z[1:rows-1,1:cols-1]  
#zz[1][1] = 11;           
print zz   

Zk1 = Z[2:rows,2:cols]            

pok = np.full( Z.shape, 0, dtype=float);
pok = Z[1:rows,1:cols] 

print zz - Zk1
print Zk1 - zz + Zk1 - zz + Zk1 - zz +Zk1 - zz