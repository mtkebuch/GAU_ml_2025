import random
import string
from csv import excel
import pandas as pd

saxeli=['mari','anano','sofo','elene']
gvari=['sanaia','kunaia','chkonia','mebonia']

data={
    "col1":random.sample(range(1,100),50),
    "col2":[random.choice(saxeli) for _ in range(50)],
    "col3":[random.choice(gvari) for _ in range(50)],
    "col4":[random.randint(2000,5000) for _ in range(50)]
}

df=pd.DataFrame(data)
df.to_excel('rowss.xlsx',sheet_name="sheetOne",index=False)

#2
df=pd.read_excel('staff_1000.xlsx')
filtered=df[df['Age']>20]

filtered.to_excel('newdata_1.xlsx',sheet_name='ages')

#3
df=pd.read_excel('staff_1000.xlsx')
filtered=df[df["First Name"].str.contains('a')]
filtered.to_excel('acont.xlsx',sheet_name='acontains')

#4
data={
   "col1":[''.join(random.choices(string.ascii_letters, k=10)) for _ in range(50)],
   "col2":[random.randint(0,10) for _ in range(50)],
   "col3":[random.randint(1,7) for _ in range(50)],
   "col4":random.sample(range(1,100),50)
}

df=pd.DataFrame(data)
df.to_excel('excel.xlsx',sheet_name='sheetOne',index=False)

#5
df=pd.read_excel('staff_1000.xlsx',sheet_name='Sheet1')
filtered=df[(df['Age']>=30) & (df['Age']<=40)]
filtered.to_excel('age3040.xlsx',sheet_name='sheetOne',index=False)


