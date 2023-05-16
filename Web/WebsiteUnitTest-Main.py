# Import the Unit Test module 
import unittest
# Could be necessary (??)
import os
import sys
import time
# Global driver that the Main routine and the test files use
import WebsiteDriverInit


# Import test files
from LoginTests import NormalLogin, TestLoginWrongEmail,TestLoginWrongPassword, TestBlankLogin,TestBlankPasswordLogin,TestBlankEmailLogin
from SignupTests import NormalSignUp,testSignUpWrongNames,testSignUpWrongEmailDomian,testSignUpWithoutPassword,testSignUpEmptyEmail,testSignUpAssociatedEmail,testSignUpDiffrentEmails,testSignUpWithoutFirstName,WeackPasswordSignUp
from EventCreationTests import NormalEventCreation, NoLocation, NoTitle,PublishEvent,PageLoading
from LogoutTest import Logout
from GUITests import ManageEventsTest,ItIsMyAccount,Likes

class MainTestingRoutine(unittest.TestCase):

    # ###################### LOGIN TESTS ##############################
    
    # def test_Login1(self): # Test Login using correct credentials
    #     NormalLogin()

    # def test_Login2(self): # Test login using incorrect credentials
    #     TestLoginWrongEmail()

    # def test_Login3(self): # Test login using incorrect credentials
    #     TestLoginWrongPassword()    

    # def test_Login4(self): # Test login with no credentials at all
    #     TestBlankLogin()

    # def test_Login5(self): # Test login with no password
    #     TestBlankPasswordLogin() 
    # def test_Login6(self):  
    #       TestBlankEmailLogin()  

    ###################### SIGNUP TESTS ##############################
    
    # def test_SignUp1(self):
    # # Test SignUp using correct credentials
    #   NormalSignUp()

    # def test_SignUp2(self):
    # # Test SignUp using incorrect credentials
    #     testSignUpWrongNames()

    # def test_SignUp3(self):
    # # Test SignUp using incorrect email domain
    #     testSignUpWrongEmailDomian()

    # def test_SignUp4(self):
    # # Test SignUp with no credentials at all
    #     testSignUpWithoutPassword()

    # def test_SignUp5(self):
    # # Test SignUp with no email
    #     testSignUpEmptyEmail()

    # def test_SignUp6(self):
    # # Test SignUp with an already associated email
    #     testSignUpAssociatedEmail()

    # def test_SignUp7(self):
    # # Test SignUp with different emails
    #     testSignUpDiffrentEmails()

    # def test_SignUp8(self):
    # # Test SignUp without a first name
    #  testSignUpWithoutFirstName()
    # def test_SignUp9(self):
    # # Test SignUp with weak password
    #  testSignUpWithoutFirstName()

    ##################### EVENT CREATION TESTS ######################

    def test_EC1(self): # Test error message when trying to save an event without a location
        NoLocation()

    def test_EC2(self): # Test error message when trying to save an event without a title
        NoTitle()

    def test_ECFinal(self): # Test Normal event creation with an online venue
        NormalEventCreation()
        
    def test_PubluishEvent(self):
        PublishEvent()
    ##################### LOG OUT TESTS ######################
    # def test_Logout(self): # Test Normal logout
    #     Logout() 
    # def test_GUI(self):       
    #   ItIsMyAccount()
    # def test_ManageEvents(self):  
    #     ManageEventsTest()
    # def test_Likes(self):  
    #     Likes()    
    # def test_relosd(self):
    #     PageLoading()
if __name__ == "__main__":
    # unittest.main()
    with open('web_test_results.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner)