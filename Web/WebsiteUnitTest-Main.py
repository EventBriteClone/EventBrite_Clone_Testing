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
from EventCreationTests import TestTagLimit, NormalEventCreation, NoLocation, TestDoubleTags, NoTitle



class MainTestingRoutine(unittest.TestCase):

    ###################### LOGIN TESTS ##############################
    
    def test_Login1(self): # Test Login using correct credentials
        NormalLogin()

    def test_Login2(self): # Test login using incorrect credentials
        TestLoginWrongEmail()

    def test_Login3(self): # Test login with no credentials at all
        BlankLogin()

    ##################### EVENT CREATION TESTS ######################

    def test_EC1(self): # Test error message when trying to enter more than 10 tags
        TestTagLimit()

    def test_EC2(self): # Test error message when trying to save an event without a location
        NoLocation()

    def test_EC3(self): # Test error message when trying to save an event without a title
        NoTitle()

    def test_EC4(self): # Test double Tagging
        TestDoubleTags()

    def test_ECFinal(self): # Test Normal event creation with an online venue
        NormalEventCreation()

        
if __name__ == "__main__":
    unittest.main()