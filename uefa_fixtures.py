import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


data = pd.read_csv('data.csv')
ids = data['Team ID'].drop_duplicates().reset_index(drop=True)

base_url = 'https://www.uefa.com/uefachampionsleague/season=2019/clubs/club='

columns = ['Round ID','Match ID','Location','Home','Away','H','A']
data_matches = pd.DataFrame(columns = columns)

for id in ids:
    url = base_url + str(id) + '/matches/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    for match in soup.find_all(class_='matches'):
        match_url = match.find(class_='match-row_link').get('href')
        parsed_url = match_url.split('/')
        rnd_parse = parsed_url[4].split('=')
        match_parse = parsed_url[5].split('=')
        r_id = rnd_parse[1]
        m_id = match_parse[1]
        loc = match.find(class_='match-location_stadium').text
        names = match.find_all(class_='team-name')
        hteam = names[0].find(class_='fitty-fit').text.strip()
        ateam = names[1].find(class_='fitty-fit').text.strip()
        hscore = match.find(class_='js-team--home-score').text
        ascore = match.find(class_='js-team--away-score').text
        fixture_data = pd.DataFrame([[r_id,m_id,loc,hteam,ateam,hscore,ascore]])
        fixture_data.columns = columns
        data_matches = data_matches.append(fixture_data,ignore_index=True)
    time.sleep(30)

data_matches.drop_duplicates()
data_matches.to_csv('fixtures.csv',index = False)