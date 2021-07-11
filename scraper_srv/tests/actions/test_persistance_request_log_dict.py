import re
from scrapers import web_scraper
import pytest
from pytest_mock import mocker

from actions import persistance_request_log_dict
from repository.mongodb_repository import MongoDBRepository
 
def test_given_false_when_persistance_request_log_dict_is_called_with_empty_url(mocker):
    url = None
    result=persistance_request_log_dict.persist_request_log(url)
    assert result==False

def test_given_persist_data_from_mongodb_repository_when_persistance_request_log_dict_is_called_with_url(mocker):
    url = "http://dummy.com"
    
    mocker.patch.object(MongoDBRepository, 'persistData')
    persistance_request_log_dict.persist_request_log(url)

    MongoDBRepository.persistData.assert_called()

def test_given_all_parameters_when_persistance_requestst_is_called_with_url(mocker):
    mocker.patch.object(web_scraper, 'get_href')
    mocker.patch.object(MongoDBRepository, 'persistData')

    url = "http://dummy.com"

    result = persistance_request_log_dict.persist_request_log(url)

    assert 'uuid' in  result
    assert 'start_date' in  result
    assert 'end_date' in  result