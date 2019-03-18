import pandas as pd

df = pd.read_csv('fixtures.csv')
df2 = pd.read_csv('data.csv')

team_id = df2[['Team', 'Team ID']].drop_duplicates().reset_index(drop=True).T

print(team_id)