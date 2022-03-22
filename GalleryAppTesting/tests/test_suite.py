import unittest
from tests.cases.login_tests import LoginTests
from tests.cases.logout_tests import LogoutTests
from tests.cases.create_gallery_tests import CreateGalleryTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CreateGalleryTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(LogoutTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
