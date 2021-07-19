from repository.mongodb_repository import MongoDBRepository
from datetime import datetime
from repository.mongodb_repository import MongoDBRepository
from scrapers.web_scraper import web_scraper
from entity.request_log import *

class RequestLog():
    
    def __init__(self, url):
        self.url = url

    def get_request_log(this, request_log_id):
        if(request_log_id):
            request_log = MongoDBRepository.getDataById(request_log_id)
            return request_log
        else:
            return False

    def get_request_log_list(this):
        list_requests = MongoDBRepository.getData()
        return list_requests

 
    def persist_request_log(this):
        if(this.url):
            start_date = datetime.now().isoformat()
            payload = web_scraper.get_href(this.url)
            end_date = datetime.now().isoformat()
            
            request_log_dict = request_log(start_date, end_date, this.url, payload)
            MongoDBRepository.persistData(request_log_dict)
            return request_log_dict
        else:
            return False