import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

df = pd.read_csv(r"C:\Users\Mylaptop.ge\Desktop\GAU_ml_2025\StudentPerformanceFactors.csv")

#1
score_avg=df['Exam_Score'].mean()
gender_count=df['Gender'].value_counts()
motivation=df['Motivation_Level'].value_counts(normalize=True)*100
studyHours_avg=df['Hours_Studied'].mean()

#2
students=pd.DataFrame({
    'name': ['Ana', 'Nini', 'Gio', 'Luka', 'Mariam'],
    'age': [20, 19, 22, 21, 20],
    'gender': ['F', 'F', 'M', 'M', 'F'],
    'hours_studied': [10, 4, 7, 2, 12],
    'subject': ['Math', 'Math', 'Math', 'Math', 'Math'],
    'passed': ['Yes', 'No', 'Yes', 'No', 'Yes']
})

students['attendance']=[90,60,80,40,95]

x=students[['age','hours_studied','attendance']]
y=students[['passed']]
print(x)
print(y)

#3
np.random.seed(5)
age=np.random.randint(18,60,50)
income=np.random.randint(500,5000,50)

df=pd.DataFrame({
    'age':age,
    'income':income
})
print(df.head())

plt.scatter(df['age'],df['income'])
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Age vs Income')
plt.show()

df['spending']=np.random.randint(200,3000,50)

plt.scatter(df['age'],df['spending'],color='pink')
plt.xlabel('Age')
plt.ylabel('Spending')
plt.title('Age vs Spending')
plt.show()

#4
score=0
directions=['left','right','forward','backward']

for i in range(10):
    move=random.choice(directions)
    if move == 'right':
        score+=1
    else:
        score-=1

print(score)

#5
df = pd.read_csv(r"C:\Users\Mylaptop.ge\Desktop\GAU_ml_2025\Housing.csv")
city=['tbilisi','qutaisi','batumi']
df['city']=[random.choice(city) for _ in range(len(df))]
print(df.head())
print(df.dtypes)

avg_price=df.groupby('city')['price'].mean()
print('average price',avg_price)

plt.scatter(df['bedrooms'],df['price'])
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.title('Bedrooms and Price')
plt.show()