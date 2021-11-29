import numpy as np

# 1D
a = np.array([1,2,4,5,8])

print(np.insert(a,1,100))
print(np.insert(a,(3,5),100))
print("###################################")

# 2D
b = np.array([ [11,12]
                ,[13,14]])
print(np.insert(b,1,50,axis=0))
print(np.insert(b,1,50,axis=1))
print(np.insert(b,1,[10,20],axis=0))