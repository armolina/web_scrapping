import requests
from bs4 import BeautifulSoup
from models import request_log
from datetime import datetime
from actions import persistance_request_log_dict

def get_href(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))

    return urls