# Import the Unit Test module 
import unittest
# Could be necessary (??)
import os
import sys
import time
# Global driver that the Main routine and the test files use
import WebsiteDriverInit


# Import test files
from LoginTests import NormalLogin, TestLoginWrongEmail, BlankLogin



class MainTestingRoutine(unittest.TestCase):

    ###################### LOGIN TESTS ##############################
    
    def test_Login1(self): # Test Login using correct credentials
        NormalLogin()

    def test_Login2(self): # Test login using incorrect credentials
        TestLoginWrongEmail()

    def test_Login3(self): # Test login with no credentials at all
        BlankLogin()


        
if __name__ == "__main__":
    unittest.main()