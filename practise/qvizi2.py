import pandas as pd
import random
import matplotlib.pyplot as plt
import random
import numpy as np


#1
name=['nini','mari','ani','salo']
gender=['male','female']
subject=['math','history','georgian','it','art']
passed=['yes','no']

data={
    "name":[random.choice(name) for _ in range(10)],
    "age":[random.randint(1,60) for _ in range(10)],
    "gender":[random.choice(gender) for _ in range(10)],
    "hours_studied":[random.randint(1,8) for _ in range(10)],
    "subject":[random.choice(subject) for _ in range(10)],
    "passed":[random.choice(passed) for _ in range(10)],
}
df=pd.DataFrame(data)
print(df)

age=df['age'].mean()
print(age)
gender_count=df['gender'].value_counts()
print(gender_count)
percent=(df['passed'].value_counts(normalize=True)['yes'])*100
print('procenti',percent)

procentino=(df['passed'].value_counts(normalize=True)['no'])*100
print(procentino)

#2
x=df[['age','hours_studied']]
print(x)
y=df['passed']
print(y)
df['attendance']=[23,21,32,31,32,21,45,98,76,54]
x_new=df[['age','hours_studied','attendance']]

#3
np.random.seed(15)

data={
    "age":np.random.randint(20,40,10),
    "income":np.random.randint(1000,2000,10)
}
df=pd.DataFrame(data)

x=df['age']
y=df['income']

plt.scatter(x,y,color='purple')
plt.xlabel('age')
plt.ylabel('income')
plt.show()

df['spending']=np.random.randint(500,2500,10)
y=df['spending']
plt.scatter(x,y,color='purple')
plt.xlabel('age')
plt.ylabel('spending')
plt.show()

#4
score=0
dir=['left','right','back','forward']

for i in range(10):
    move=random.choice(dir)
    if move=='right':
        score+=1
    else:
        score-=1

print(score)

#5
df = pd.read_csv(r"C:\Users\mtkeb\Desktop\GAU_ml_2025\laboratories\real-estate.csv")
print(df.dtypes)
avg_by_city=df.groupby('city')['price'].mean()
print(avg_by_city)
avg_by_rooms=df.groupby('state')['price'].mean()
print(avg_by_rooms)

plt.scatter(df['bed'],df['price'],color="red")
plt.xlabel('bed')
plt.ylabel('price')
plt.title('city and price')
plt.show()

