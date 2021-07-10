import sys
import json
from pymongo import MongoClient

def get_entity_list():
    try:
        client = MongoClient("127.0.0.1", 27017)
        db = client.scraper_database
        collection = db["scraper_logs"]
        
        requests = []
        for request in collection.find({}):
            requests.append(request["uuid"])
        
        return requests
    except Exception as e:
        sys.stderr.write("Exception in persist in list_request_log_dict: %s " % e) 
        raise e