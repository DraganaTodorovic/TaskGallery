import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class CreateGalleryPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _create_gallery_link = "Create Gallery"
    _title_field = "title"
    _description_field = "description"
    _image_url_field = "//*[@id='app']/div[2]/div/div/form/div[3]/div/div/input"
    _add_image_button = "//*[@id='app']//button[text()='Add image']"
    _submit_button = "//*[@id='app']//button[text()='Submit']"
    _cancel_button = "//*[@id='app']//button[text()='Cancel']"
    _message = "//*[@id='app']//p[text()='Wrong format of image']"
    _title_style = "//*[@id='app']//h1[text()='All Galleries']"


    def clickCreateGalleryLink(self):
        self.elementClick(self._create_gallery_link, locatorType="link")

    def enterTitle(self, title):
        self.sendKeys(title, self._title_field)

    def enterDescription(self, description):
        self.sendKeys(description, self._description_field)

    def enterImageUrl(self, image_url):
        self.sendKeys(image_url, self._image_url_field, locatorType="xpath")

    def clickAddImageButton(self):
        self.elementClick(locator=self._add_image_button, locatorType="xpath")

    def clickSubmitButton(self):
        self.elementClick(locator=self._submit_button, locatorType="xpath")

    def clickCancelButton(self):
        self.elementClick(locator=self._cancel_button, locatorType="xpath")

    def cancel(self, title="", description="", image_url=""):
        self.clickCreateGalleryLink()
        self.enterTitle(title)
        self.enterDescription(description)
        self.enterImageUrl(image_url)
        self.clickCancelButton()

    def submit(self, title="", description="", image_url=""):
        self.clickCreateGalleryLink()
        self.enterTitle(title)
        self.enterDescription(description)
        self.enterImageUrl(image_url)
        self.clickSubmitButton()

    def verifyAddedImageSuccessful(self):
        result = self.isElementPresent(self._title_style, locatorType="xpath")
        return result

    def verifyAddedImageFailed(self):
        result = self.isElementPresent(self._message, locatorType="xpath")
        return result

    def verifyImageUlrFailed(self):
        result = self.isElementPresent(self._message, locatorType="xpath")
        return result


