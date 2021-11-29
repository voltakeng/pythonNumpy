import numpy as np 

# zero matrix 
zero = np.zeros((3,2,1) ,dtype=int)
#print(zero)
print("#################################")

# ones matrix 
ones = np.ones((3,3), dtype=int)
#print(ones)
print("#################################")

# constant matrix 
cons = np.full((3,3), 7)
#print(cons)
print("#################################")

# empty matrix 
empty = np.empty((3,4), int)
#print(empty)
print("#################################")

# identiry matrix 
identity = np.identity(5, float)
#print(identity)
print("#################################")

# eye matrix 
eye = np.eye(3,4,k=1)
#print(eye)
eye = np.eye(3,4,k=-1)
#print(eye)
print("#################################")

# linspace matrix
linspace = np.linspace(1,10)
#print(linspace)
linspace = np.linspace(1,10,4)
#print(linspace)
linspace = np.linspace(1,5,endpoint=False)
#print(linspace)
print("#################################")

# arange matrix 
arange = np.arange(-7,14,2, dtype=int)
#print(arange)

# random matrix 
random = np.random.random((2,2))
print(random)