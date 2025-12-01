from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('StudentsPerformance.csv')
x=df[['math score']]
y=df[['reading score']]

model=LinearRegression()
model.fit(x,y)
print('math and reading score linear',model.score(x,y))

poly=PolynomialFeatures(degree=2)
x_poly=poly.fit_transform(x)

model=LinearRegression()
model.fit(x_poly,y)
print('mat and reading score poly',model.score(x_poly,y))

