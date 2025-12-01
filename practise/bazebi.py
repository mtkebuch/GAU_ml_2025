import random

import mysql.connector
import pandas as pd

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="uni_db"
)

cursor=mydb.cursor()

#1
query="INSERT INTO students(name,lastname,gpa) VALUES(%s,%s,%s)"
val=('mari','tyebuchava','2.3')
cursor.execute(query,val)
mydb.commit()

#2
q="INSERT INTO students(name,lastname,gpa) VALUES(%s,%s,%s)"
saxeli=['mari','ani','lola']
gvari=['tyebuchava','todua','gogochuri']
students=[]

for i in range(10):
    name=random.choice(saxeli)
    lastname=random.choice(gvari)
    gpa=round(random.uniform(1,4),2)
    students.append((name,lastname,gpa))

cursor.executemany(q,students)
mydb.commit()

#3
q="SELECT * FROM students WHERE name='mari'"
cursor.execute(q)
rows=cursor.fetchall()

for row in rows:
    print(row)

df=pd.DataFrame(rows)
df.to_excel('maris.xlsx',sheet_name='mari',index=False)

