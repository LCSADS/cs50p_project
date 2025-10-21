import pytest
from entities import User
from storage import user_to_dict,dict_to_user,save_user,load_users

test_user = "test_user"
test_hash = "$pbkdf2-sha256$29000$5vwfw7hXCsGYcw4BwDjH2A$H6yt1NJo.SzhiBjnbCH6zOVc/cMx6wwjBz7ZMvdgcWU"

def test_user_to_dict():
    user_object = User(username=test_user,password_hash=test_hash)
    user_dictionary = user_to_dict(user_object)
    assert user_dictionary['username'] == test_user
    assert user_dictionary['password_hash'] == test_hash


def test_dict_to_user():
    test_dict = {'username': test_user,'password_hash': test_hash}
    user_object = dict_to_user(test_dict)
    assert isinstance(user_object,User)
    assert user_object._password_hash == test_hash
    assert user_object.username == test_user
