import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

df=pd.read_csv('StudentsPerformance.csv')

rxm=df['reading score'].corr(df['math score'])
print(rxm)
rxw=df['reading score'].corr(df['writing score'])
print(rxw)
#
# plt.scatter(df['reading score'],df['math score'],color="pink")
# plt.xlabel('reading score')
# plt.ylabel('math score')
# plt.title('reading score and math score')
# plt.show()
#
# plt.scatter(df['reading score'],df['writing score'],color='green')
# plt.xlabel('reading score')
# plt.ylabel('writing score')
# plt.title('reading and writing')
# plt.show()

#2
df=pd.read_csv('Salary_Data.csv')
salExp=df['YearsExperience'].corr(df['Salary'])
print(salExp)

#3
df=pd.read_csv('advertising.csv')
x=df[['TV','Radio','Newspaper']]
y=df['Sales']
model=LinearRegression()
model.fit(x,y)
print('coeff',model.coef_)
print('intercept',model.intercept_)

#4
df=pd.read_csv('data.csv')
x=df[['bedrooms','bathrooms','condition']]
y=df['price']
model=LinearRegression()
model.fit(x,y)
print('coeff',model.coef_)
print('intercept',model.intercept_)

#5
df=pd.read_csv('co2.csv')
x=df[['Fuel Consumption Hwy (L/100 km)','Fuel Consumption Comb (L/100 km)','Engine Size(L)']]
y=df['CO2 Emissions(g/km)']
model=LinearRegression()
model.fit(x,y)
print('coeff',model.coef_)
print('intercept',model.intercept_)

#6
df=pd.read_csv('StudentsPerformance.csv')
x=df[['reading score']]
ymath=df['math score']
ywrite=df['writing score']

model=LinearRegression()
model.fit(x,ymath)
print('readingnmath',model.score(x,ymath))
model.fit(x,ywrite)
print('readingnwrite',model.score(x,ywrite))

poly=PolynomialFeatures(degree=2)
x_poly=poly.fit_transform(x)
model=LinearRegression()
model.fit(x_poly,ymath)
print('poly model score',model.score(x_poly,ymath))

poly=PolynomialFeatures(degree=2)
x_poly=poly.fit_transform(x)
model=LinearRegression()
model.fit(x_poly,ywrite)
print('poly model writing score',model.score(x_poly,ywrite))

#7

df=pd.read_csv('student_data.csv')
x=df[['studytime','health','G1']]
y=df['G3']

model=LinearRegression()
model.fit(x,y)
print('linear model score',model.score(x,y))

poly=PolynomialFeatures(degree=2)
x_poly=poly.fit_transform(x)
model=LinearRegression()
model.fit(x_poly,y)
print('polynomial model score',model.score(x_poly,y))
