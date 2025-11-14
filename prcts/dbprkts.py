import mysql.connector
import pandas as pd
import random

mydb=mysql.connector.connect(
    host="localhost",
    password="",
    user="root",
    database="uni_db"
)

cursor=mydb.cursor()

#1
# sql="INSERT INTO books (title,author,price) VALUES (%s,%s,%s)"
# val=("akaki","gamzrdeli",10)
# cursor.execute(sql,val)
# mydb.commit()

#2
sql="INSERT INTO students(name,lastname,gpa) VALUES(%s,%s,%s)"
books=[]
names=["oreo","kindera","snikersa","baunta","twixa"]
lastnames=["oreoshvili","kinderashvili","snikersashvili","bauntashvili","twixashvili"]

for _ in range(10):
    name=random.choice(names)
    lastname=random.choice(lastnames)
    gpa=round(random.uniform(1,100),1)
    books.append((name,lastname,gpa))

cursor.executemany(sql,books)
mydb.commit()

#3
query="SELECT * FROM students WHERE name='baunta'"
cursor.execute(query)
rows=cursor.fetchall()
for row in rows:
    print(row)

df=pd.DataFrame(rows)
df.to_excel('rows.xlsx')

