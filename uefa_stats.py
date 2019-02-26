import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


data = pd.read_csv('fixtures.csv')
fix = data[['Round ID','Match ID']].drop_duplicates().reset_index(drop=True)

base_url = 'https://www.uefa.com/uefachampionsleague/season=2019/matches/round='

columns = ['Round ID', 'Match ID', 'Team', 'Title,Stats']
data_stats = pd.DataFrame(columns=columns)

for index,row in fix.iterrows():
  rnd = row['Round ID']
  id = row['Match ID']
  url = base_url + str(rnd) + '/match=' + str(id) + '/index.html'
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  if(soup.find(class_='team-name_name home') != None):
    hteam = soup.find(class_='team-name_name home').text
    table = soup.find(class_='live-stats-home')
    for row in table.find_all(class_='stats-row bottom-row'):
      title = row.find(class_='stats-title-home').text.strip()
      stat = row.find(class_='stats-data-home').text.strip()
      stats_data = pd.DataFrame([[rnd,id,hteam,(title,stat)]])
      stats_data.columns = columns
      data_stats = data_stats.append(stats_data,ignore_index=True)
  elif(soup.find(class_='team-name_name away') != None): 
    ateam = soup.find(class_='team-name_name away').text
    table = soup.find(class_='live-stats-away')
    for row in table.find_all('stats-row bottom-row'):
      title = row.find(class_='stats-title-away').text.strip()
      stat = row.find(class_='stats-data-away').text.strip()
      stats_data = pd.DataFrame([[rnd,id,ateam,(title,stat)]])
      stats_data.columns = columns
      data_stats = data_stats.append(stats_data,ignore_index=True)
  else:
    stats_data = pd.DataFrame([[rnd,id,None,None]])
    stats_data.columns = columns   
    data_stats = data_stats.append(stats_data,ignore_index=True)
  
  time.sleep(30)

data_stats.drop_duplicates()
data_stats.to_csv('stats.csv',index = False)  
