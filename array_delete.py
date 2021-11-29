import numpy as np 

a = np.arange(1,11)
print(np.delete(a,2))
print('########################')

b = np.arange(1,13).reshape(4,3)
print(np.delete(b,2,axis=0))
print(b)