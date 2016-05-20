import requests,bs4

def getValue(url_link):

    res = requests.get(url_link)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text)
    eles = soup.select('article.takeAction:nth-child(1) > h2:nth-child(1)')
    return eles[0].text


datadata = getValue('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts')

print('The Ctual value is'+data)           
