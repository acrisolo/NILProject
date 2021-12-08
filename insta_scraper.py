from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.instagram.com/tombrady/"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

followers = html_soup.find_all('div', class_="g47SY")

filename = 'followers.csv'
f = open(filename, 'w')

headers = 'Number of Followers \n'
f.write(headers)


for comps in followers.find('div', class_= "-nal3 "):
    number = followers.find('div', class_="-nal3 ")
    f.write(number)

f.close()
    

