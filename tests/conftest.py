import pytest
from entities import User
import storage
import json
import factory

class Fake_Sequencial_Inputs:
    def __init__(self,inputs):
        self.inputs = list(inputs)
        self.index = 0
    
    def __call__(self,prompt):
        if self.index >= len(self.inputs):
            raise IndexError("No more fake inputs provided")
        input = self.inputs[self.index]
        self.index += 1
        return input

@pytest.fixture
def fake_input_sequence():
# fake sequencial inputs factory
    def fake_input_factory(inputs):
        return Fake_Sequencial_Inputs(inputs)
    return fake_input_factory
        
@pytest.fixture
def valid_username():
    return "lucas"

@pytest.fixture
def invalid_username():
    return "thisusernameiswaytoobig!!!!!!"

@pytest.fixture
def valid_password():
    return "V@lidPassw0rd"

@pytest.fixture
def invalid_password():
    return "invalid"


@pytest.fixture()
def storage_setup_with_user(monkeypatch,tmp_path,valid_username,valid_password):
# create temp path to use a temp json file for tests
    temp_json = tmp_path / "test_user.json"
# modifies the json_path variable inside storage > user_storage temporarily so that we can test without touching the actual json file
# syntax for monkeypatch is package/module/variable
    monkeypatch.setattr("storage.user_storage.json_path", temp_json)
# creates and saves the new user on the temp path and temp json
    test_user = factory.create_user(valid_username,valid_password)
# save_user uses the temp path because of the monkeypatch
    storage.save_user(test_user)
    return test_user

@pytest.fixture
def mock_load_users(monkeypatch,valid_user):
    def mock():
        return [valid_user]
    monkeypatch.setattr(storage.user_storage,"load_users",mock)
    return mock

@pytest.fixture
def storage_setup_with_dict(monkeypatch,tmp_path,valid_user_dict):
    temp_json = tmp_path / "test_user.json"
    monkeypatch.setattr(storage.user_storage,"json_path", temp_json)
    temp_json.write_text(json.dumps([valid_user_dict]))

@pytest.fixture
def valid_user_dict(valid_username,valid_hash):
    return {'username': valid_username,'password_hash': valid_hash}

@pytest.fixture
def valid_hash():
    return "valid_test_hash"

@pytest.fixture
def valid_user(valid_username,valid_hash):
    return User(username=valid_username,password_hash=valid_hash)
