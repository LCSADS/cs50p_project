import pytest
from entities import User
import storage
import json


def test_user_to_dict(valid_user):
    user_dictionary = storage.user_to_dict(valid_user)
    assert user_dictionary['username'] == valid_user.username
    assert user_dictionary['password_hash'] == valid_user._password_hash

def test_dict_to_user(valid_user_dict):
    test_dict = valid_user_dict
    user_object = storage.dict_to_user(test_dict)
    assert isinstance(user_object,User)
    assert user_object.username == test_dict['username']
    assert user_object._password_hash == test_dict['password_hash']

def test_load_users(storage_setup_with_dict):
    result = storage.load_users()
    assert result != []
    assert isinstance(result[0],User)

def test_save_user_isolated(monkeypatch,tmp_path,mock_load_users):
    temp_json = tmp_path / "test_file.json"
    monkeypatch.setattr(storage.user_storage,"json_path",temp_json)

    new_user = User(username="test_user",password_hash="test_hash")

    storage.save_user(new_user)

    with open(temp_json,"r") as file:
        temp_data = json.load(file)
# two users, one mocked in load users and another created during the test to save
    assert len(temp_data) == 2
    assert temp_data[1]["username"] == "test_user"
    assert temp_data[1]["password_hash"] == "test_hash"

def test_find_user(mock_load_users,valid_username):
    found_user = storage.find_user(valid_username)
    assert found_user.username == valid_username

def test_check_username_existence(monkeypatch,valid_username,valid_user):
    def mock_find_user(username):
        if username == valid_username:
            return valid_user
        else:
            return None
    monkeypatch.setattr(storage.user_storage,"find_user",mock_find_user)
    username_exists = storage.check_username_existence(valid_username)
    non_existent_username = storage.check_username_existence("ghost")
    assert username_exists == True
    assert non_existent_username == False

def test_save_user_integrated(storage_setup_with_dict,tmp_path,valid_user,valid_username):
    temp_json = tmp_path / "test_user.json"
    storage.user_storage.json_path = temp_json
    new_user = User(username="new_test_user",password_hash="new_test_hash")
    storage.save_user(new_user)
    with open(temp_json,"r") as file:
        temp_user_list = json.load(file)
    assert len(temp_user_list) == 2
    usernames = []
    for user in temp_user_list:
        usernames.append(user["username"])
    assert "new_test_user" in usernames
    assert valid_username in usernames



