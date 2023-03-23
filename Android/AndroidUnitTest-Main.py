# import the Unit Test module
import unittest
# could be necessary (??)
import os
import sys
import time
# Global driver that the Main routine and the test files use
import AndroidDriverInit
# Import test files
import TestAndroidTitle


class EvenBriteSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AndroidDriverInit.driver

    def test_Sample(self):
        TestAndroidTitle.SampleTest()

    def tearDown(self):
        if self.driver:
            self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()