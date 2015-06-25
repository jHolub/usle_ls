import numpy as np
import time

start = time.time() 

Z = np.array([
            [10,9,8,7,5],
            [11,10,8,7,5],
            [12,9,8,9,10],
            [13,9,8,7,5]
            ])

#Z = np.arange(1000000).reshape(1000,1000)

nodata = 9999
#    Z2    Z6    Z3
#    Z8    Z     Z7
#    Z4    Z5    Z1

rows,cols = len(Z), len(Z[0])

Zk1 = np.full(Z.shape,nodata, dtype=int);
Zk1[0:rows-1,0:cols-1] = Z[1:rows,1:cols]
#print Zk1
Zk2 = np.full(Z.shape,nodata, dtype=int);
Zk2[1:rows,1:cols] = Z[0:rows-1,0:cols-1]
#print Zk2

Zk3 = np.full(Z.shape,nodata, dtype=int);
Zk3[1:rows,0:cols-1] = Z[0:rows-1,1:cols]
#print Zk3
Zk4 = np.full(Z.shape,nodata, dtype=int);
Zk4[0:rows-1,1:cols] = Z[1:rows,0:cols-1]
#print Zk4

Zk5 = np.full(Z.shape,nodata, dtype=int);
Zk5[0:rows-1,0:cols] = Z[1:rows,0:cols]
#print Zk5
Zk6 = np.full(Z.shape,nodata, dtype=int);
Zk6[1:rows,0:cols] = Z[0:rows-1,0:cols]
#print Zk6

Zk7 = np.full(Z.shape,nodata, dtype=int);
Zk7[0:rows,0:cols-1] = Z[0:rows,1:cols]
#print Zk7
Zk8 = np.full(Z.shape,nodata, dtype=int);
Zk8[0:rows,1:cols] = Z[0:rows,0:cols-1]
#print Zk8

vaha = ( ((Z - Zk1) + abs(Z - Zk1)) + ((Z - Zk2) + abs(Z - Zk2)) + ((Z - Zk3) + abs(Z - Zk3)) + ((Z - Zk4) + abs(Z - Zk4)) + ((Z - Zk5) + abs(Z - Zk5)) + ((Z - Zk6) + abs(Z - Zk6)) + ((Z - Zk7) + abs(Z - Zk7)) + ((Z - Zk8) + abs(Z - Zk8))) / 2
print vaha





print 'It took', time.time()-start, 'seconds.' 
