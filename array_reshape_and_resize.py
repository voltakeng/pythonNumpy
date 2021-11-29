import numpy as np 

a = np.arange(10) 

# reshape จะเปลี่ยนแปลงชั่วคราว
print(a.reshape((2,5)))

b = a.reshape((2,5))
print(b)
print(a)
print("#################################")

# resize จะเปลี่ยนแปลงถาวร
a.resize((2,5))
print(a)


