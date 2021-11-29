import numpy as np 

x = np.arange(1,10)

index = np.array([1,5,7])
print(x[index])

m = x[[1,4,1,4,1,4,1,4]]
print(m)

x = np.array([[1,-2,3],[4,-5,-6]])
print(x[x>0])
print(x[x>2])
print(x[x<0]**2)