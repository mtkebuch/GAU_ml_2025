import pandas as pd
import random
import string

rows=100
#1 [expression for variable in range(n)]

col1=[''.join(random.choices(string.ascii_letters,k=10)) for _ in range (rows)]
col2=[random.randint(0,10) for _ in range (rows)]
col3=[random.randint(1,7) for _ in range (rows)]
col4=random.sample(range(1,101),rows)

df = pd.DataFrame({
    'Col1':col1,
    'Col2':col2,
    'Col3':col3,
    'Col4':col4
})

df.to_excel('data.xlsx',sheet_name='sheetOne',index=False)

#2

df=pd.read_excel('data.xlsx',sheet_name='sheetOne')
df_new=df[df['Col1'].str.contains('a')]
df_new.to_excel('datanew.xlsx',sheet_name='sheet3',index=False)

#3

df=pd.read_excel('staff_1000.xlsx', sheet_name='Sheet1')
df_new=df[(df['Age']>=30) & (df['Age']<=40)]
df_new.to_excel('staff_age.xlsx',sheet_name='sheetOne',index=False)





