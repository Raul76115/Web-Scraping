import pandas as pd
import numpy as numpy

df = pd.read_csv('stats.csv')
df1 = df['Title,Stats'].str[1:-1].str.split(',',expand=True)
df1.columns = ['Event','Stat']
df2 = df.drop(['Title,Stats'],axis=1)
frames = [df2,df1]

result = pd.concat(frames,axis=1)

df3 = result['Stat'].str.split()

for row in df3:
    if(isinstance(row,list) and len(row) > 1):
        del row[1]
    elif(isinstance(row,float) != True):
        row.insert(0,None)


df4 = result.drop(['Stat'],axis =1)
frames1 = [df4,df3]

result1 = pd.concat(frames1,axis=1)

df5 = result1['Stat'].apply(pd.Series)
df0 = df5[0].str.extract(r'(\d+)')
df1 = df5[1].str.extract(r'(\d+)')
df1.columns = [1]
df6 = result1.drop(['Stat'],axis=1)
frames2 = [df6,df0,df1]

result2 = pd.concat(frames2,axis=1)

print(result2.head(10))
