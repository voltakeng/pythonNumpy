# กรณีที่ มิติของ array 2 ตัวไม่เหมือนกัน มันจะบวกลบกันไม่ได้
# ตัวที่เล็กกว่าเลยจะ ขยายตัวขึ้นมา เพื่อให้บวกกันได้

import numpy as np 

x = np.array([ [1,2]
                ,[3,4]
                ,[5,6] ])

y = np.array([ [1,2] ])
print(x+y)

y = np.array([2])
print(x+y)

y = np.array([ [10]
                ,[20] 
                ,[30] ])
print(x+y)

y = np.array( [10,20] )
print(x+y)