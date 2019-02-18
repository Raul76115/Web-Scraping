import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'https://en.wikipedia.org/wiki/2018%E2%80%9319_UEFA_Champions_League'
page = requests.get(url)

columns = ['Team']
data_teams = pd.DataFrame(columns = columns)

soup = BeautifulSoup(page.text, 'html.parser')
tables = soup.find_all(class_='wikitable')

for index in range(21,29):
    rows = tables[index].find_all('tr')
    for row in range(1,len(rows)):
      td = rows[row].find_all('td')
      a = td[0].find_all('a')
      team = a[1].text
      team_data = pd.DataFrame([[team]])
      team_data.columns = columns
      data_teams = data_teams.append(team_data,ignore_index=True)


