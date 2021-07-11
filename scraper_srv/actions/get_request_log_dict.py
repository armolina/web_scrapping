from repository.mongodb_repository import MongoDBRepository

def get_request_log(request_log_id):
    if(request_log_id):
        request_log = MongoDBRepository.getDataById(request_log_id)
        return request_log
    else:
        return False