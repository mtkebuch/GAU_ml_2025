import mysql.connector
import random
import pandas as pd

mydb=mysql.connector.connect(
    user="root",
    database="uni_db",
    host="localhost",
    password=""
)

#1
#ბაზასთან ბრძანებების გაშვების საშუალება.
cursor=mydb.cursor()

sql="INSERT INTO students(name,lastname,gpa) VALUES(%s,%s,%s)"
val=("ana","tyebuchava",2.1)

cursor.execute(sql,val)
mydb.commit()

#2
sql="INSERT INTO students(name,lastname,gpa) VALUES(%s,%s,%s)"

names=['mari','anano','nino','anuka','elene','liza','qeti']
last_name=['tyebuchava','jolokhava','nemswveridze','gogochuri']
students=[]

for _ in range(50):
    name=random.choice(names)
    lastname=random.choice(last_name)
    gpa=round(random.uniform(0,4),2)
    students.append((name,lastname,gpa))

cursor.executemany(sql,students)
mydb.commit()

#3
sql="SELECT * FROM students WHERE name='mari'"
cursor.execute(sql)
rows=cursor.fetchall()
for row in rows:
    print(row)

df=pd.DataFrame(rows)
df.to_excel("rows.xlsx",index=False)

cursor.close()
mydb.close()
