from pages.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    def test_validLogin(self):
        self.lp.login("gallery_app_test@yahoo.com", "Test12345")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result1, "Login Verification")

    def test_validLogout(self):
        self.lp.logout()
        result = self.lp.verifyLogoutSuccessful()
        assert result == True

    def test_invalidLogin(self):
        self.lp.login("gallery_app_test@yahoo.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True

