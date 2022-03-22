from pages.create_gallery_page import CreateGalleryPage
from pages.login_page import LoginPage
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CreateGalleryTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.cgp = CreateGalleryPage(self.driver)

    def test_invalidCreatedGallery(self):
        self.lp.login("gallery_app_test@yahoo.com", "Test12345")
        time_srt = str(round(time.time() * 1000))
        image_title = "Delfin " + time_srt
        image_description = "Image added: " + time_srt
        self.cgp.submit(title=image_title, description=image_description, image_url="c:\work\invalide_image_type.jpg")
        result = self.cgp.verifyImageUlrFailed()
        assert result == True

    def test_validCreatedGallery(self):
        # self.lp.login("gallery_app_test@yahoo.com", "Test12345")
        time_srt = str(round(time.time() * 1000))
        image_title = "Delfin " + time_srt
        image_description = "Image added: " + time_srt
        new_image_url = "https://opusteno.rs/slike/2015/12/zanimljivosti-o-delfinima-28839/zanimljivosti-o-delfinima-sp.jpg"
        self.cgp.submit(title=image_title, description=image_description, image_url=new_image_url)
        result = self.cgp.verifyAddedImageSuccessful()
        assert result == True


