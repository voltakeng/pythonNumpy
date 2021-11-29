import numpy as np 

# 1D
arr = np.array([1,2,3]) 
print(arr.ndim)

li = [1,2,3,4]
b = np.array(li)
print(b)


# 2D
arr_2d = np.array([ [1,2,3],[4,5,6] ])
print(arr_2d)
print(arr_2d.ndim)


# 3D
li_3d = [ [ 
           [1,2,3],
           [4,5,6] 
       ],
       [
           [7,8,9],
           [10,11,12]
       ]         
    ]

a = np.array(li_3d)
print(a)
print(a.ndim)

