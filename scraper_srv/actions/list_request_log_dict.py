import sys
import os
import json
from repository.mongodb_repository import MongoDBRepository

def get_request_log_list():
    list_requests = MongoDBRepository.getData()
    return list_requests