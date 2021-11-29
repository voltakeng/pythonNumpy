import numpy as np 

a = np.array([3,4,2,6])
b = np.array([8,6,5,10])

c = np.concatenate( (a,b) )
print(c)

a = np.append(a,500)
print(a)

d = np.array([ [11,12]
                ,[13,14]])
d = np.append(d, [[10,20]],axis=1)
print(d)