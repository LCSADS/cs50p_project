import pytest
from hasher import hasher,verify_password

@pytest.fixture
def valid_password():
    return "V@lidPassw0rd"

def test_password_hashing(valid_password):
    password_hash = hasher(valid_password)
    assert isinstance(password_hash,str)
    assert len(password_hash) > 60
    assert password_hash != valid_password

def test_password_accepted(valid_password):
    password_hash = hasher(valid_password)
    assert verify_password(valid_password,password_hash) is True

def test_password_denied(valid_password):
    invalid_password = "invalidpassword"
    password_hash = hasher(valid_password)
    assert verify_password(invalid_password,password_hash) is False



