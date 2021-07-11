import requests
from bs4 import BeautifulSoup

def get_href(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))

    return urls