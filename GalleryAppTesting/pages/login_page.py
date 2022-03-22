import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//*[@id='app']//button[text()='Submit']"
    _logout_link = "Logout"
    _message = "//*[@id='app']//p[text()='Bad Credentials']"


    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(locator=self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._logout_link, locatorType="link")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._message, locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Gallery App")

    def logout(self):
        self.elementClick(self._logout_link, locatorType="link")

    def verifyLogoutSuccessful(self):
        result = self.isElementPresent(self._login_link, locatorType="link")
        return result

