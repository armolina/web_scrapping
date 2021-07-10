import sys
import os
import json
from pymongo import MongoClient

def get_entity():
    try:
        client = MongoClient(os.environ['DB_HOST'], 27017)
        db = client.scraper_database
        collection = db["scraper_logs"]

        return collection.find_one({"uuid":"bb76e474-e111-11eb-a2bd-6ba2bd379764"}, {"_id":0})
    except Exception as e:
        sys.stderr.write("Exception in get_requests_log_dict %s " % e) 
        raise e