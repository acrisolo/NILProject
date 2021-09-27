#Writes completion scores and years in a file called completion_scores.csv tab delimited
from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.espn.com/college-football/player/stats/_/id/4034607/liam-welch"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

body = html_soup.find('table', class_="Table Table--align-right")
header = html_soup.find('table', class_="Table Table--align-right Table--fixed Table--fixed-left")

filename = 'completion_rates.csv'
f = open(filename, 'w')

headers = 'Completion Scores \n'
f.write(headers)
 
for heads in header.find_all('tbody'):
    lines = heads.find_all('tr')
    for line in lines:
        year = line.find_all('td', class_="Table__TD")[0].text
        f.write(year + "\t")

f.write("\n")

for comps in body.find_all('tbody'):
    rows = comps.find_all('tr')
    for row in rows:
        comp_scores = row.find_all('td', class_="Table__TD")[2].text
        f.write(comp_scores + "\t")

f.close()
