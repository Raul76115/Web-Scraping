import pandas as pd

df1 = pd.read_csv('lineups_f.csv').drop('Round',axis = 1)
df2 = pd.read_csv('fixtures.csv')

result = pd.merge(df2,df1,how = 'inner',on = 'Match ID')

print(result.head())