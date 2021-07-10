import os
import sys
from pymongo import MongoClient

class MongoDBRepository:
    def __connect():
        client = MongoClient(os.environ['DB_HOST'], 27017)
        db = client.scraper_database
        collection = db["scraper_logs"]
        return collection

    def getDataById(value_to_search):
        try:
            collection = MongoDBRepository.__connect()
            return collection.find_one({"uuid":value_to_search}, {"_id":0})
        except Exception as e:
            sys.stderr.write("Exception in getDataById: %s " % e) 
            raise e
    
    def getData():
        try:
            collection = MongoDBRepository.__connect()

            requests = []
            for request in collection.find({}):
                requests.append(request["uuid"])
            
            return requests
        except Exception as e:
            sys.stderr.write("Exception in getData: %s " % e) 
            raise e
    
    def persistData(request_log):
        try:
            MongoDBRepository.collection = None
            collection = MongoDBRepository.__connect()
            collection.insert_one(request_log)
        except Exception as e:
            sys.stderr.write("Exception in persistData: %s " % e) 
            raise e