import pytest
from hasher import hasher,verify_password


# test pass hashing with the fixed $pbkdf2-sha256$ that comes at the start of each hash, ensuring it's a valid pbkdf2-sha256 as implemented

def test_password_hashing(valid_password):
    password_hash = hasher(valid_password)
    assert isinstance(password_hash,str)
    assert password_hash.startswith("$pbkdf2-sha256$")
    assert password_hash != valid_password
    assert len(password_hash) > 60


# test if the salt works, two hashes of the same password should have different outcomes

def test_hash_is_salted(valid_password):
    first_hash = hasher(valid_password)
    second_hash = hasher(valid_password)
    assert first_hash != second_hash


# test verify password variations with parametrize

@pytest.mark.parametrize(
    ("password_input","expected_output"),
    [
        ("V@lidPassw0rd",True),
        ("invalidpassword",False),
        ("",False),
    ],
)

def test_verify_password(valid_password,password_input,expected_output):
    hash = hasher(valid_password)
    validation = verify_password(password_input,hash)
    if expected_output is True:
        assert validation is True
    else:
        assert validation is False





