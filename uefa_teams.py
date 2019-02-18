import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'https://www.uefa.com/uefachampionsleague/season=2019/standings/round=2000980/#grp-2006091'
page = requests.get(url)

columns = ['Team ID','Group','Team','Short']
data_teams = pd.DataFrame(columns = columns)

soup = BeautifulSoup(page.text, 'html.parser')
for group in soup.find_all(class_='group-container'):
  extra_span = group.find(class_='live-now').decompose()
  group_name = group.find(class_='group-name').text.strip()
  for table in group.find_all(class_='table table--standings'):
    tbody = table.find('tbody')
    for row in tbody.find_all('tr'):
        team_id = row.get('data-team-id')
        td = row.find_all('td')
        extra_span = td[0].find(class_='now-playing_label').decompose()
        team = td[0].find(class_='team-name js-team-name').text.strip()
        short = td[0].find(class_='team-code').text
        team_data = pd.DataFrame([[team_id,group_name,team,short]])
        team_data.columns = columns
        data_teams = data_teams.append(team_data,ignore_index=True)


base_url = 'https://www.uefa.com/uefachampionsleague/season=2019/clubs/'

columns = ['Team_ID','Position','Name']
data_players = pd.DataFrame(columns = columns)

for id in data_teams['Team ID']:
  url = base_url + 'club=' + id + '/squad/'
  page = requests.get(url)
  soup = BeautifulSoup(page.text,'html.parser')
  tables = soup.find_all(class_='squad--team-wrap')
  for index in range(1,5):   
    pos = tables[index].find('h5').text
    tbody = tables[index].find('tbody')
    for row in tbody.find_all('tr'):
      td = row.find('td')
      player = td.find(class_='player-name').text.strip()
      players_data = pd.DataFrame([[id,pos,player]])
      players_data.columns = columns
      data_players = data_players.append(players_data,ignore_index=True)
time.sleep(30)

print(data_players.tail())

#full_data = pd.merge(data_teams,data_players,how = 'inner', on = 'Team ID')
#full_data.to_csv('data.csv')