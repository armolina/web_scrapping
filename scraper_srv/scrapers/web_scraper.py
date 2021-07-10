import requests
from bs4 import BeautifulSoup
from models import request_log
from datetime import datetime
from actions.persistance_request_log_dict import PersistanceRequestLogDict

def get_href(url):
    start_date = datetime.now().isoformat()

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    
    
    end_date = datetime.now().isoformat()

    request_log_dict = request_log.request_log(start_date, end_date, "web", "href", urls)
    PersistanceRequestLogDict.persist_entity(request_log_dict)
    return request_log_dict