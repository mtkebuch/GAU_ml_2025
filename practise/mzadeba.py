import numpy as np
import random
import pandas as pd
import string
import mysql.connector

#numpy
#1
text='mariamityebuchava'
n=3
parts=[text[i:i+n] for i in range(0,len(text),n)]
print(parts)

#2
x=np.random.randint(1,100,(2,2))
y=np.random.randint(1,100,(2,2))
z=x+y
print(z)

x=np.array([[1,2],[2,3]])
y=np.array([[2,5],[2,7]])
z=np.dot(x,y)
print(z)

#3
# matrix=np.random.randint(0,10,(10,10))
# print(matrix)
# num=int(input("sheiyvanet ricxvi"))
# matrix[matrix==num]=0
# print(matrix)

#4
matrix=np.zeros((8,8),dtype=int)
matrix[1::2,::2]=1
matrix[::2,1::2]=1
print(matrix)

#pandas
names=['mari','nini','anuki','salo']
data={
    "ricxvebi":random.sample(range(1,100),6),
    "name":[random.choice(names) for _ in range(6)],
    "nums":[random.randint(1,100) for _ in range(6)]
}
df=pd.DataFrame(data)
df.to_excel('data.xlsx',sheet_name='sheetTwo')

read=pd.read_excel('data.xlsx',sheet_name='sheetTwo')

filter=read[read['name'].str.contains('a')]
print(filter)

read_1=pd.read_excel('staff_1000.xlsx')
filter_1=read_1[(read_1['Age']>=30) & (read_1['Age']<=40) ]
print(filter_1)

#
data={
    'saxeli':['mari','ana','sofo'],
    'gvari':['tyebuchava','jolokhava','ujirauli']
}
print(data)


arr=np.array([[1,2,3,4],[2,3,4,5]])
print(arr[0,:2])
print(arr[1,:3])

matrix=np.random.randint(1,10,(3,3))
print(matrix)

#7
x=int(input('sheiyvanet ricxvi:'))
if x % 10 ==0:
    print('ricxvi bolovdeba nulit')
else:
    print('ricxvi ar bolovdeba nulit')

#11
for i in range(20,125):
    if i % 5 ==0:
        print(i)

#14
nums=[]
for i in range(10):
    nums.append(random.randint(1,100))

print(nums)

nums=[]
for i in range(10):
    num=input('ricxvi:')
    nums.append(num)

print(nums)

num=(input('ricxvi'))
print(len(num))

#lab2_2
a=input('a:')
b=input('b:')
c=input('c:')
print(max(a,b,c))

#6
nums=[]
for _ in range(10):
    nums.append(random.randint(1,10))

print(nums)


