import pytest
from factory import create_user
from entities import User


def test_object_creation(valid_username,valid_password):
    new_user = create_user(valid_username,valid_password)
    assert new_user is not None
    assert isinstance(new_user,User)

def test_object_contains_hash(valid_username,valid_password):
    new_user = create_user(valid_username,valid_password)
    assert hasattr(new_user,'_password_hash')
    assert len(new_user._password_hash) > 50
    assert new_user._password_hash != valid_password

def test_user_creation_invalid_password(valid_username):
    invalid_password = "invalid"
    new_user = create_user(valid_username,invalid_password)
    assert new_user is None

def test_user_creation_invalid_username(valid_password):
    invalid_username = "meia"
    new_user = create_user(invalid_username,valid_password)
    assert new_user is None
