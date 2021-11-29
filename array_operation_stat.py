import numpy as np 

# 1D
a = np.array( [10,5,4,6,99,100,50,30] )
print(a.sum())
print(a.prod())
print(a.mean())
print(a.max())
print(a.min())
print(a.argmax())
print(a.argmin())

# 2D
b = np.array([ [10,20,30]
                ,[40,50,90]
                ,[80,100,5] ])
print( np.min(b,axis=1) )
print( np.max(b,axis=0) )




