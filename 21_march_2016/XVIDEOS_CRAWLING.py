import requests
from bs4 import BeautifulSoup
def my_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.yahoo.com' #s+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        #for i in plain_text:
            #print(i,end='')
        soup = BeautifulSoup(plain_text)
        for link in soup.findall('a'):#, {'class': 'lzbg'}):
            href = link.get('href')
            title = link.string
            print(title)
            print(href)
        #page += 1

my_spider(1)
