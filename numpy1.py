import random
import numpy as np
import string
import pandas as pd
import mysql.connector

#
# #1
# text='ilovemybf'
# n=3
# parts=[text[i:i+n] for i in range(0,len(text),n)]
# print(parts)
#
# #2
# x=np.array([[1,2,3,5],[2,3,4,1]])
# y=np.array([[1,2,3,5],[2,3,4,1]])
# c=x+y
# print(c)
#
# x=np.random.randint(1,10,(2,2))
# y=np.random.randint(1,10,(2,2))
# c=np.dot(x,y)
# print(c)
#
# #3
# matrix=np.random.randint(1,10,(10,10))
# print(matrix)
# x=int(input("sheiyvanet wasashleli ricxvi:"))
# matrix[matrix==x]=0
# print(matrix)
#
# #4
# arr=np.array([1,2,3,4])
# print(arr[1:])
#
# #5
# matrix=np.zeros((8,8),dtype=int)
# print(matrix)
#
# matrix[1::2,::2]=1
# matrix[::2,1::2]=1
# print(matrix)


#pandas
name=['mari','bani','ani']
data={
    "col1":[''.join(random.choices(string.ascii_letters,k=10)) for _ in range(50)],
    "col2":random.sample(range(1,100),50),
    "col3":[random.randint(1,100) for _ in range(50)],
    "col4":[random.choice(name) for _ in range(50)]

}

df=pd.DataFrame(data,columns=["col1","col2","col3","col4"])
df.to_excel('lastrow1s.xlsx',sheet_name="sheeOne",index=False)

rows=pd.read_excel('staff_1000.xlsx')

filtered=rows[rows['First Name'].str.contains('a')]
filtered.to_excel('rowss.xlsx',sheet_name='sheet',index=False)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    database="uni_db",
    password=""
)

#1
cursor=mydb.cursor()
sql="INSERT INTO students(name,lastname,gpa) VALUES(%s,%s,%s)"
val=("marikuna","tkebuchava",2.1)

cursor.execute(sql,val)
mydb.commit()

#2random
query="INSERT INTO students(name,lastname,gpa) VALUES(%s,%s,%s)"

saxeli=['mari','anuki','nini']
gvari=['tyebu','jolokhava','germanishvili']

students=[]

for _ in range(10):
    name=random.choice(saxeli)
    surname=random.choice(gvari)
    gpas=round(random.uniform(0,4),2)
    students.append((name,surname,gpas))

cursor.executemany(sql,students)
mydb.commit()

#3
query="SELECT * FROM students WHERE gpa>3"
cursor.execute(query)
rows=cursor.fetchall()
for row in rows:
    print(row)

df=pd.DataFrame(rows)
df.to_excel('lastorw.xlsx',sheet_name="gpa under 3",index=False)


