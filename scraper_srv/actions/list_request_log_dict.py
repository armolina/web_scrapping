import sys
import os
import json
from pymongo import MongoClient

def get_entity_list():
    try:
        client = MongoClient(os.environ['DB_HOST'], 27017)
        db = client.scraper_database
        collection = db["scraper_logs"]
        
        requests = []
        for request in collection.find({}):
            requests.append(request["uuid"])
        
        return requests
    except Exception as e:
        sys.stderr.write("Exception in persist in list_request_log_dict: %s " % e) 
        raise e