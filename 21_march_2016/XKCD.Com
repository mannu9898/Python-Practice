import bs4, requests

def getPrice(producturl):
    res = requests.get(producturl)
    res.raise_for_status()


    soup = bs4.BeautifulSoup(res.text,'html.parser')
    eles = soup.select('.sphinxsidebarwrapper > p:nth-child(3)')
    return eles[0].text.strip()



#for i in range(1660,1675):
price = getPrice('http://docs.python-requests.org/en/master/user/install/')

print('The price is '+price)
