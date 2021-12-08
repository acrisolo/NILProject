from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://platform.affinio.com/reports/287802473669189196/0/287802473669189196_17/interests/index"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')
global_scores = html_soup.find_all('div', id='ember20104', class_="bottomscore")

filename = 'global_scores.csv'
f = open(filename, 'w')

headers = 'Global Scores \n'
f.write(headers)
 
for global_rel in global_scores.find_all('strong', class_='affinity-score'):
        f.write(global_rel + "\t")

f.close()

