import requests
from bs4 import BeautifulSoup
class web_scraper():
    def get_href(url: str):

        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        
        urls = []
        for link in soup.find_all('a'):
            urls.append(link.get('href'))

        return urls