import re
import pytest
from pytest_mock import mocker

from actions import get_request_log_dict
from repository.mongodb_repository import MongoDBRepository
 
def test_given_false_when_get_request_is_called_with_empty_id(mocker):
    request_log_id = None
    result=get_request_log_dict.get_request_log(request_log_id)
    assert result==False

def test_given_get_data_by_id_in_mongo_repository_when_get_request_is_called_with_filled_id(mocker):
    request_log_id = "dummyID"
    
    mocker.patch.object(MongoDBRepository, 'getDataById')
    get_request_log_dict.get_request_log(request_log_id)

    MongoDBRepository.getDataById.assert_called()