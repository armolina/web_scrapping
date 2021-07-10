import sys
import os
from pymongo import MongoClient

class PersistanceRequestLogDict():
    def persist_entity(request):
        try:
            client = MongoClient(os.environ['DB_HOST'], 27017)
            db = client.scraper_database
            collection = db["scraper_logs"]

            return collection.insert_one(request)
        except Exception as e:
            sys.stderr.write("Exception in persist in persistance_request_log_dict: %s " % e) 
            raise e