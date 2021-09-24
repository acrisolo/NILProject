from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.espn.com/college-football/player/_/id/4034607/liam-welch"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

table = html_soup.find_all('div', class_="StatBlockInner__Value tc fw-medium n3 clr-gray-02")

filename = 'products.csv'
f = open(filename, 'w')

headers = 'Completion Scores \n'
f.write(headers)


for comps in table:
    comp_scores = table.find('div', class_="Table__TH")
    f.write(comp_scores)

f.close()
    

