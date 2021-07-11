import pytest
from pytest_mock import mocker

from repository.mongodb_repository import MongoDBRepository
 
def test_existing_exception_in_get_data_by_id(mocker):
    with pytest.raises(Exception):
        value_to_search = "some_value"
        MongoDBRepository.getDataById(value_to_search)

def test_existing_exception_in_get_data(mocker):
    with pytest.raises(Exception):
        MongoDBRepository.getData()

def test_existing_exception_in_persist_data(mocker):
    with pytest.raises(Exception):
        request_log = "some_value"
        MongoDBRepository.persistData(request_log)