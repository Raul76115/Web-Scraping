import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time


urlpage = 'https://www.scoreboard.com/soccer/europe/champions-league/standings/?t=zLZKqTTF&ts=lEbZ3p60'
driver = webdriver.PhantomJS()

driver.get(urlpage)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

time.sleep(30)

results = driver.find_elements_by_xpath("//*[@id='glib-stats-data']//*[contains(@id,'box-table-type-1')]//*[@class='stats-table-container']//*[@class='team_name_span']")
print('Number of results', len(results))

data = []

for result in results:
    team_name = result.text
    data.append({"Team":team_name})

driver.quit()
df = pd.DataFrame(data)
print(df)