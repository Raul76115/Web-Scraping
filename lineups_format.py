import pandas as pd
import numpy as numpy

df = pd.read_csv('lineups.csv')

df1 = df['Player'].str.extract(r'(\w+)')

df['Player'] = df1.values

df.to_csv('lineups_f.csv',index =False)