import mysql.connector
import random
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
val=('gode','gogotchuri','2.3')

cursor.execute(query,val)
mydb.commit()

#2
saxeli=['ani','nini','mari','soso','gigi']
gvari=['gaia','aia','baia']
students=[]

for i in range(10):
    name=random.choice(saxeli)
    surname=random.choice(gvari)
    gpa=round(random.uniform(1,4),2)
    students.append((name,surname,gpa))

cursor.executemany(query,students)
mydb.commit()

#3
query="SELECT gpa FROM students"
cursor.execute(query)
rows=cursor.fetchall()
df=pd.DataFrame(rows)
df.to_excel('students.xlsx')

for row in rows:
    print(row)

count=len(rows)
print(count)

avg=df[0].mean()
print(avg)