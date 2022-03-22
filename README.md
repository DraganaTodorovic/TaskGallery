"# TaskGallery" 

# Gallery-App Testing

## Setup

* Clone project "GalleryAppTesting" from GitHub on host machine
* To download and install `python` (python-3.10.2-amd64.exe) (I placed my instalation of python in folder "C:\Python")
* To download and install `selenium`, run this command from the terminal : `pip install selenium`
* To download and install `pytest`, run this command from the terminal : `pip install pytest`
* To download and install `requests`, run this command from the terminal : `pip install requests`
* To download and install `jsonpath`, run this command from the terminal : `pip install jsonpath`
* To download and install `pycharm` (pycharm-community-2021.3.2.exe)
* To download driver ChromeDriver for Chrome, unzip and copy exe-file ("chromedriver.exe") to folder "C:\webdriver_browsers" (this can set as Environment Variables for Path) NOTE: Check browser version and download the right driver version (example, for Chrome version: 98.0.4758.82 (Official Build) (64-bit), driver version: 98.0.4758.102 or 98.0.4758.80 -> chromedriver_win32.zip)
* Open project "GalleryAppTesting" in PyCharm and than open File->Setting... from Menu in PyCharm. From left side opened window, select "Project: GalleryAppTesting" -> "Python Interpreter". On right side, choose and select "python.exe" from folder where you placed instalation of python (in my case, it is "C:\Python\python.exe"). Click on button "Apply" and wait to load finished. After finished, you should see installed selenium, pytest, requests and their versions. Then from left side opened window, select "Tools -> "Terminal" and uncheck option Active virtualenv on right side opened Settings window.


## Info

* For testing Gallery App application, I created project "GalleryAppTesting" in PyCharm and wrote automated tests for UI testing using Selenium in Python.
* Tests are in "GalleryAppTesting\tests\cases" and:
* Automated tests for 1a with test "login_tests".
* Automated tests for 2a with test "create_gallery_tests".
* Automated tests for 4a with test "logout_tests".
* I wrote Test Suite by name "test_suite" which contains this automated test cases. Test suite is found in "GalleryAppTesting\tests" .

* During testing I used credentials:
username: gallery_app_test@yahoo.com
password: Test12345

## Running tests for UI testing

For running automated tests, I used Terminal from PyCharm (project "GalleryAppTesting" should be opened in PyCharm).

Command line for running one test is:
pytest .\tests\cases\name_of_test.py

name_of_test can be name of one of three automated tests.

Command line for running test suite is:
pytest .\tests\test_suite.py


## Running tests for API testing

I didn't write API automated tests, I tested API call only with Postman.
