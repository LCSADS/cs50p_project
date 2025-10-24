from auth import login
import pytest
from factory import create_user
from storage import load_users,save_user
import storage
from entities import User



def test_login_success(storage_setup_with_user,valid_username,valid_password):
# uses valid user and valid pass to login on the user created in the fixture above.
    login_success = login(valid_username,valid_password)
# checks if login returns something, and checks if it's a valid User object.
    assert login_success is not None
    assert isinstance(login_success,User)

def test_login_fail_password(storage_setup_with_user,valid_username):
    invalid_password = "invalid"
    assert login(valid_username,invalid_password) is None

def test_login_fail_user(storage_setup_with_user,valid_password):
    invalid_username = "meia"
    assert login(invalid_username,valid_password) is None