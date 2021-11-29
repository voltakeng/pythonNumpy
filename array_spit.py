import numpy as np 

a = np.arange(1,21)
b = np.split(a,4)
print(b)
print(b[0])
print("#######################")

a = a.reshape(5,4)

b = np.hsplit(a,4)
print(b)
print("#######################")
b = np.vsplit(a,5)
print(b)
print(b[0])
print("#######################")