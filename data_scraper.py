import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    result = {}
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    tables = soup.find('table')
    names = tables.find_all('span', class_="ds-text-tight-s ds-font-regular ds-text-typo-primary hover:ds-text-typo-primary-hover ds-block")
    stat = tables.find_all('strong')

    for i in range(len(names)):
        result[names[i].text.split(' ')[-2]] = int(stat[i+1].text)
    
    return result
