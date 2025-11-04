import random
import mysql.connector
import pandas as pd

mydb=mysql.connector.connect(
    host="localhost",
    password="",
    user="root",
    database="uni_db"
)

cursor=mydb.cursor()

sql="INSERT INTO students(name,lastname,gpa) VALUES(%s,%s,%s)"
val=('jemali','nodia',4.1)
cursor.execute(sql,val)
mydb.commit()

#2
sql="INSERT INTO students(name,lastname,gpa) VALUES(%s,%s,%s)"
saxeli=['mari','nini','elene','sofo']
gvari=['todua','ninishvili','sofashvili']

students=[]

for _ in range(6):
    name=random.choice(saxeli)
    lastname=random.choice(gvari)
    gpa=round(random.uniform(0,4),2)
    students.append((name,lastname,gpa))

cursor.executemany(sql,students)
mydb.commit()

#3
sql="SELECT * FROM students WHERE name='elene'"
cursor.execute(sql)
rows=cursor.fetchall()
for x in rows:
    print(x)

df=pd.DataFrame(rows)
df.to_excel('rows.xlsx',sheet_name='sheetOne')

count=len(rows)
print(count)


