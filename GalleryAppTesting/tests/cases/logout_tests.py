from pages.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LogoutTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    def test_validLogoutPage(self):
        self.lp.login("gallery_app_test@yahoo.com", "Test12345")
        self.lp.logout()
        result = self.lp.verifyLogoutSuccessful()
        self.ts.markFinal("test_validLogoutPage", result, "Logout Verification")
