# Tests (copy to tests/test_user_functions.py)
import pytest
import io
from code import *

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'
    
def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_twoats(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@@adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_twoats(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('pe!!tra@a!!daltas.com'))
    assert get_email_from_input() is None

# Do the same for the following functions
# Functions in src/user_functions.py and tests in tests/test_user_functions.py

def get_user_name_from_input():
    """ Not empty string. No spaces. """
    return input("Create your user name: ")

def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    return input("Create your password: ")