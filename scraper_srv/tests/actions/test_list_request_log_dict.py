import re
import pytest
from pytest_mock import mocker

from actions import list_request_log_dict
from repository.mongodb_repository import MongoDBRepository

def test_given_get_data_from_mongodb_repository_when_persistance_request_log_dict_is_called_with_url(mocker):
    mocker.patch.object(MongoDBRepository, 'getData')
    list_request_log_dict.get_request_log_list()

    MongoDBRepository.getData.assert_called()