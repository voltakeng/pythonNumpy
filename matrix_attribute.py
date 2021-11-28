import numpy as np 

a = np.array([1,2,3,4,5])
b = np.array(([1,2,3], [4,5,6], [7,8,9]))

print(a.ndim)
print(str(b.dtype))

print(a.shape)
print(b.shape)

print(a.size)
print(b.size)

print(a.itemsize)
print(b.itemsize)