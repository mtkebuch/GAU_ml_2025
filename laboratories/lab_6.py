import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

#1
df = pd.read_csv(r"C:\Users\mtkeb\Downloads\StudentsPerformance.csv")

#reading,math
corr1=df['reading score'].corr(df['math score'])
print('reading,math correlation',corr1)

#reading, writing
corr2=df['reading score'].corr(df['writing score'])
print('reading,writing',corr2)

#2
df = pd.read_csv(r"C:\Users\mtkeb\Downloads\Salary_Data.csv")
corr3=df['YearsExperience'].corr(df['Salary'])
print('years experience and salary',corr3)

#3
df=pd.read_csv(r"C:\Users\mtkeb\Downloads\advertising.csv")
x=df[["TV","Radio","Newspaper"]]
y=df["Sales"]
model=LinearRegression()
model.fit(x,y)
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

#4
df=pd.read_csv(r"C:\Users\mtkeb\Downloads\data.csv")
x=df[["bedrooms","bathrooms","sqft_living"]]
y=df["price"]
model=LinearRegression()
model.fit(x,y)
print("Coefficient",model.coef_)
print("Intercept:",model.intercept_)

#5
df=pd.read_csv(r"C:\Users\mtkeb\Downloads\auto-mpg.csv")
x=df[["cylinders","displacement","weight","acceleration","model year","origin"]]
y=df["mpg"]
model=LinearRegression()
model.fit(x,y)
print("Coeff",model.coef_)
print("Inter",model.intercept_)

#6
df=pd.read_csv(r"C:\Users\mtkeb\Downloads\co2.csv")
x=df[["Cylinders","Fuel Consumption Comb (L/100 km)","Engine Size(L)"]]
y=df["CO2 Emissions(g/km)"]
model=LinearRegression()
model.fit(x,y)
print(model.coef_)
print(model.intercept_)

#7
df=pd.read_csv(r"C:\Users\mtkeb\Downloads\StudentsPerformance.csv")
x=df[["reading score"]]
y_math=df["math score"]
y_write=df["writing score"]

#linear regression
lin=LinearRegression()

lin.fit(x,y_math)
print('lin reading math',lin.score(x,y_math))

lin.fit(x,y_write)
print('lin reading writing',lin.score(x,y_write))

#polynomial regression (degree 2)
poly=PolynomialFeatures(degree=2)

x_poly=poly.fit_transform(x)
poly_lin=LinearRegression()

poly_lin.fit(x_poly,y_math)
print('poly reading math',poly_lin.score(x_poly,y_math))

poly_lin.fit(x_poly,y_write)
print('poly reading write',poly_lin.score(x_poly,y_write))

#8
df=pd.read_csv(r"C:\Users\mtkeb\Downloads\student_data.csv")
x = df[["studytime", "failures", "absences", "G1", "G2"]]
y = df["G3"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Linear regression
lin = LinearRegression()
lin.fit(x_train, y_train)
print("Linear R2:", lin.score(x_test, y_test))

# Polynomial regression degree 2
poly = PolynomialFeatures(degree=2, include_bias=False)
x_train_p = poly.fit_transform(x_train)
x_test_p = poly.transform(x_test)

poly_lin = LinearRegression()
poly_lin.fit(x_train_p, y_train)
print("Polynomial R2:", poly_lin.score(x_test_p, y_test))