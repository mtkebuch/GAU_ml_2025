import pandas as pd
from sklearn.linear_model import LinearRegression

#1
df = pd.read_csv(r"C:\Users\Mylaptop.ge\Downloads\StudentsPerformance.csv")

#reading,math
corr1=df['reading score'].corr(df['math score'])
print('reading,math correlation',corr1)

#reading, writing
corr2=df['reading score'].corr(df['writing score'])
print('reading,writing',corr2)

#2
df = pd.read_csv(r"C:\Users\Mylaptop.ge\Downloads\Salary_Data.csv")
x=df[["YearsExperience"]]
y=df["Salary"]
model=LinearRegression()
model.fit(x,y)
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

#3
df=pd.read_csv(r"C:\Users\Mylaptop.ge\Downloads\advertising.csv")
x=df[["TV","Radio","Newspaper"]]
y=df["Sales"]
model=LinearRegression()
model.fit(x,y)
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

#4
