#!c:/canopy/User/python.exe  
import time
print "Content-type: text/html"
print
start = time.time()
s = []
for i in range(0,1000):
    r = []
    for j in range(0,1000):
        r.append((i**0.5)**0.2)
    s.append(r)
print 'It took', time.time()-start, 'seconds.' 

import numpy as np
L = range(1000)

[i**2 for i in L]

a = np.arange(1000)

b = a**2
print b

import matplotlib.pyplot as plt  # the tidy way
x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)       # line plot    
plt.show()    