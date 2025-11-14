import mysql.connector
import random
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ml_db_2025"

)
mycursor = mydb.cursor()
print(mydb)
print(mycursor)

#1
# sql = "INSERT INTO students (name, lastname, gpa) VALUES (%s, %s, %s)"
# val = ("Mariam", "Tkebuchava", 3.9)
# mycursor.execute(sql, val)
# mydb.commit()
#
# #chaweret 50 shemtxveviti monacemi,saxeli,gvari,gpa-[0;4]
#
# first_names=["Mariam", "Giorgi", "Nino", "Luka", "Ana", "David", "Tamar", "Levan", "Sopho", "Irakli"]
# last_names = ["Tkebuchava", "Beridze", "Kapanadze", "Giorgadze", "Mchedlishvili", "Tsiklauri", "Gvasalia", "Japaridze"]
#
# for _ in range(50):
#     name=random.choice(first_names)
#     lastname=random.choice(last_names)
#     gpa=round(random.uniform(0,4),2)
#     val=(name,lastname,gpa)
#     mycursor.execute(sql,val)
#
# mydb.commit()
# print("Inserted 50 random students")
#
#3 waikitxet students cxrilis monacemebi da gpa.xlsx failshi gadaitanet im studentebis monacemebi ,visi gpa-c 2-ze metia, gamotvalet aseti studentebis raodenoba monacemebit chaweret gpas mixedvit zrdadobit
