import re
import pytest
from policies import password_policy,security_feedback,username_policy

def test_valid_password():
    assert password_policy("V@l1ddPassword") is True

def test_invalid_password():
    assert password_policy("invalidpassword") is False


def test_valid_username():
    assert username_policy("Lucas123") is True

def test_invalid_username():
    assert username_policy("luuuuuuuuucaaaaaaaaaasssssssss!!!") is False

def test_security_feedback_all_failures(capsys):
    weak_password = ""
    security_feedback(weak_password)
    output = capsys.readouterr().out
    assert "At least one capital letter." in output
    assert "At least one lower letter." in output
    assert "At least one special character" in output
    assert "At least one number" in output
    assert "Lenght between 8 and 16 characters." in output


def test_security_feedback_missing_uppercase(capsys):
    weak_password = "invalidp@ssw0rd"
    security_feedback(weak_password)
    output = capsys.readouterr().out
    assert "At least one capital letter." in output


def test_security_feedback_missing_lowercase(capsys):
    weak_password = "INVALIDP@SSW0RD"
    security_feedback(weak_password)
    output = capsys.readouterr().out
    assert "At least one lower letter." in output
    

def test_security_feedback_missing_special_character(capsys):
    weak_password = "Invalidpassw0rd"
    security_feedback(weak_password)
    output = capsys.readouterr().out
    assert "At least one special character" in output

def test_security_feedback_missing_number(capsys):
    weak_password = "Invalidp@assword"
    security_feedback(weak_password)
    output = capsys.readouterr().out
    assert "At least one number" in output


def test_security_feedback_under_min_lenght(capsys):
    weak_password = "Wr0ng!"
    security_feedback(weak_password)
    output = capsys.readouterr().out
    assert "Lenght between 8 and 16 characters." in output


def test_security_feedback_over_max_lenght(capsys):
    weak_password = "thispasswordiswaytoolong"
    security_feedback(weak_password)
    output = capsys.readouterr().out
    assert "Lenght between 8 and 16 characters." in output