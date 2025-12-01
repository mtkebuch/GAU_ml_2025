import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('student_data.csv')
avg_age=df['age'].mean()
print(avg_age)

count=df['Pstatus'].value_counts()
print(count)

percent=(df['Pstatus'].value_counts(normalize=True))*100
print(percent)

plt.scatter(df['age'],df['sex'],color='pink')
plt.xlabel('age')
plt.ylabel('sex')
plt.title('age and sex')
plt.show()