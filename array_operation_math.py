import numpy as np 

a = np.arange(1,5)
print(a+2)
print(a*3)

b = np.arange(1,5)
print(a+b) #shapeต้องเท่ากัน

c = np.arange(1,10)
#print(b+c) จะทำไม่ได้

x = np.array([ [1,2,3],
                [4,5,6] ])
print(x+[2])


