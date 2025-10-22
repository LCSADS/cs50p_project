from auth import login
import pytest
from factory import create_user
from storage import load_users,save_user
import storage
from entities import User

@pytest.fixture
def valid_username():
    return "testuser"

@pytest.fixture
def valid_password():
    return "V@lidPassw0rd"

@pytest.fixture()
def storage_setup(monkeypatch,tmp_path,valid_username,valid_password):
# create temp path to use a temp json file for tests
    temp_json = tmp_path / "test_user.json"
# modifies the json_path variable inside storage > user_storage temporarily so that we can test without touching the actual json file
# syntax for monkeypatch is package/module/variable
    monkeypatch.setattr("storage.user_storage.json_path", temp_json)
# creates and saves the new user on the temp path and temp json
    test_user = create_user(valid_username,valid_password)
# save_user uses the temp path because of the monkeypatch
    save_user(test_user)
    return test_user



def test_login_success(storage_setup,valid_username,valid_password):
# uses valid user and valid pass to login on the user created in the fixture above.
    login_success = login(valid_username,valid_password)
# checks if login returns something, and checks if it's a valid User object.
    assert login_success is not None
    assert isinstance(login_success,User)

def test_login_fail_password(storage_setup,valid_username):
    invalid_password = "invalid"
    assert login(valid_username,invalid_password) is None

def test_login_fail_user(storage_setup,valid_password):
    invalid_username = "meia"
    assert login(invalid_username,valid_password) is None