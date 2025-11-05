import numpy as np


matrix=np.random.randint(0,10,(10,10))
print(matrix)
num=int(input('sheikvanet ricxvi'))
matrix[matrix==num]=0
print(matrix)

#2
x=np.array([[1,2,3],[3,2,1]])
y=np.array([[2,3,2],[5,6,5]])
z=x+y
print(z)

list=np.array([1,2,3,4,4,7])
print(list[0:4])



