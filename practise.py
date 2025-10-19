import numpy as np

arr=np.array([2,4,5,6])
print(type(arr))

arr_1=np.array([[1,2,3],[2,3,4]])
print(arr_1)

arr_2=np.array([
    [[5,4,3],[7,5,4],[8,9,6]],
    [[7,2,1],[9,3,4],[6,4,6]]
])
print(arr_2)

print(arr_2.ndim)

print(arr[0])
print(arr_1[0,1])

#[start:end:step]