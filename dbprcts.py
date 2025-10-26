import mysql.connector
import random
import pandas as pd

mydb=mysql.connector.connect(
    host="localhost",
    password="",
    database="books_library",
    user="root"
)

#1
mycursor=mydb.cursor()

sql="INSERT INTO books(title,author,price)VALUES(%s,%s,%s)"
val=("pride and prejudice","jane austen",15)

mycursor.execute(sql,val)
mydb.commit()

sql="INSERT INTO books(title,author,price)VALUES(%s,%s,%s)"
val=("witelquda","ucnobi",10)
mycursor.execute(sql,val)
mydb.commit()

#2
sql = "INSERT INTO books (title, author, price) VALUES (%s, %s, %s)"
titles = ["Pride and Prejudice", "Hamlet", "1984", "The Hobbit", "The Alchemist"]
authors = ["Jane Austen", "William Shakespeare", "George Orwell", "J.R.R. Tolkien", "Paulo Coelho"]

books=[]
for _ in range(50):
    title=random.choice(titles)
    author=random.choice(authors)
    price=round(random.uniform(1,100),2)
    books.append((title,author,price))

mycursor.executemany(sql,books)
mydb.commit()


#3

query="SELECT title,author,price FROM books WHERE price > 50"

mycursor.execute(query)
rows=mycursor.fetchall()
print(rows)


df=pd.DataFrame(rows,columns=["Title","Author","Price"])
df.to_excel("books_over_50.xlsx",index=False)

count=len(df)
avg=round(sum(df['Price'])/count,2)

print("monacemebi excel-shi chaiwera")
print("jamshi aseti aris:",count)
print("avg aris:",avg)

mycursor.close()
mydb.close()
