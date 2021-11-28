import numpy as np 

a = np.array([1,2,3,4,5])
print(a[0])
print(a[-1])

b = np.array([[1,2,3],[4,5,6]])
print(b[0][2])

li = [ [ 
           [1,2,3],
           [4,5,6] 
       ],
       [
           [7,8,9],
           [10,11,12]
       ]         
    ]
c = np.array(li) 

dept = 1
row = 0
column = 2 

print(c[dept][row][column])
