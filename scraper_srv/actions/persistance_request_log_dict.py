from datetime import datetime
from repository.mongodb_repository import MongoDBRepository
from scrapers.web_scraper import web_scrapper
from models.request_log import *
 
def persist_request_log(url):
    if(url):
        start_date = datetime.now().isoformat()
        payload = web_scrapper.get_href(url)
        end_date = datetime.now().isoformat()
        
        request_log_dict = request_log(start_date, end_date, url, payload)
        MongoDBRepository.persistData(request_log_dict)
        return request_log_dict
    else:
        return False