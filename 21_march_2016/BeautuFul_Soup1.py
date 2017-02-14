import bs4, requests

def getPrice(producturl):
    res = requests.get(producturl)
    res.raise_for_status()


    soup = bs4.BeautifulSoup(res.text,'html.parser')
    eles = soup.select('div.comment:nth-child(5) > div:nth-child(2) > a:nth-child(1)')
    return eles[0].text.strip()



price = getPrice('element')

print('The price is '+price)
