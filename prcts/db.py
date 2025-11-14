import random

import mysql.connector
import pandas as pd

mydb=mysql.connector.connect(
    user="root",
    host="localhost",
    password="",
    database="shop_db"
)

mycursor=mydb.cursor()

#1
sql="INSERT INTO products(name,price,amount) VALUES(%s,%s,%s)"
val=("puri",2,50)
mycursor.execute(sql,val)
mydb.commit()

print(mycursor.rowcount)

#2
sql="INSERT INTO products(name,price,amount) VALUES(%s,%s,%s)"

products=[]
names=['qindzi','marwyvi','xinkali','mwvadi','kitri']

for _ in range(50):
    name=random.choice(names)
    price=round(random.uniform(1,100),2)
    amount=random.randint(1,100)
    products.append((name,price,amount))

mycursor.executemany(sql,products)
mydb.commit()

#3
sql="SELECT * FROM products WHERE price>50"
mycursor.execute(sql)
rows=mycursor.fetchall()

df=pd.DataFrame(rows)
df.to_excel("data.xlsx",index=False)

sql="SELECT * FROM products WHERE price=2"
mycursor.execute(sql)
rows=mycursor.fetchall()

df=pd.DataFrame(rows)
df.to_excel("data_1.xlsx",index=False)


