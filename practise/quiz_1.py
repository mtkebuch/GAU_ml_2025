import random
import numpy as np
import pandas
import pandas as pd

#1
nums=[]

for i in range(15):
    nums.append(random.randint(10,100))

print(nums)

new_nums=[]
for x in nums:
    if x % 7 !=0:
        new_nums.append(x)

print(new_nums)


#2
arr=np.random.randint(1,51,(6,6))
print(arr)
for x in arr:
    print(np.mean(x))

new_arr=arr**2

print(new_arr)

#3
names=['ana','mari','lizi']
department=['it','hr']

data={
    "names":[random.choice(names) for _ in range(15)],
    "department":[random.choice(department) for _ in range(15)],
    "salary":[random.randint(1500,4000) for _ in range(15)],
    "joiningYear":[random.randint(2015,2025) for _ in range(15)]

}

df=pd.DataFrame(data)

print(df)

df.to_excel('employees.xlsx')

read_excel=pd.read_excel('employees.xlsx')
print(read_excel)

filter=df[(df['salary']>2500) & ((df['department']=='it') | (df['department']=='hr'))]
print(filter)

sorted=df.sort_values(by="salary",ascending=False)
print(sorted)

print("5 data",sorted.head(5))


