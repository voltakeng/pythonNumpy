# convert 2D to 1D

import numpy as np 

a = np.array([ [1,2]
                ,[3,4]
                ,[5,6] ])

b = a.flatten()

print(a)
print(b)
print("###################################")

# เมื่อเปลี่ยนค่าใน c ค่าใน a จะเปลี่ยนตาม
c = a.ravel()
c[0] = 5 

print(a)
print(b)
print(c)
print("###################################")