# test_addition.py
from testcase_main import valid_login , browser_close
import pytest

def test_validlogin():
    global output
    output = valid_login()
    assert output == 5
    browser_close()


