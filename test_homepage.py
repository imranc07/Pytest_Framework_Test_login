from homepage import LoginTest
import pytest

# URL for automation testing
url = "https://practicetestautomation.com/practice-test-login/"
test_login = LoginTest(url)

# Method for checking Positive Testing
def test_valid_login():
    expected_url = "https://practicetestautomation.com/practice-test-login/"
    assert test_login.login() == True


# Method for checking Negative Testing with wrong username
def test_NegativeUsernam():
    expected_url = "https://practicetestautomation.com/logged-in-successfully/"
    assert test_login.NegativeUsername() == True

# Method for checking Negative Testing with wrong password
def test_NegativePasswo():
    expected_url = "https://practicetestautomation.com/logged-in-successfully/"
    assert test_login.NegativePassword() == True
    