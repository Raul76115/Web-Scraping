import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


data = pd.read_csv('fixtures.csv')
rnds = data['Round ID'].drop_duplicates().reset_index(drop=True)
ids = data['Match ID'].drop_duplicates().reset_index(drop=True)
base_url = 'https://www.uefa.com/uefachampionsleague/season=2019/matches/round='

columns = ['Round','Match_ID','Player','Events','Time']
data_lineups = pd.DataFrame(columns = columns)

for rnd in rnds:
  for id in ids:
    url = base_url + str(rnd) + '/match=' + str(id) + '/lineups/index.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    for lineups in soup.find_all(class_='squad--team-list'):
      for li in lineups.find_all('li'):
        if(li.find(class_='fitty-fit') != None):
          name = li.find(class_='fitty-fit').text.split()
          if(li.find(class_='lineups--events') != None):
            for event in li.find_all(class_='lineups--events-event'):
              desc = event.find('img').get('title')
              minute = event.find('span').text
              lineup_data = pd.DataFrame([[rnd,id,name,desc,minute]])
              lineup_data.columns = columns
              data_lineups = data_lineups.append(lineup_data,ignore_index=True)
          else:
            lineup_data = pd.DataFrame([[rnd,id,name,None,None]])
            lineup_data.columns = columns
            data_lineups = data_lineups.append(lineup_data,ignore_index=True)
  time.sleep(30)

data_lineups.to_csv('lineups.csv',index = False)