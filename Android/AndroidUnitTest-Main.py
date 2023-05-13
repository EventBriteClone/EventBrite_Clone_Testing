# import the Unit Test module
import unittest
# could be necessary (??)
import os
import sys
import time
import random, string
# Global driver that the Main routine and the test files use
import AndroidDriverInit
# Import test files
import GenericAndroidTests

RandomEventName = ''.join(random.choices(string.ascii_letters + string.digits, k=10))


class EvenBriteSearch(unittest.TestCase):

    ############################### SIGN UP TESTS #########################

    def test_SUnoAt(self): #test sign up with invalid email
        GenericAndroidTests.SignUpNoAt()
    
    def test_SU(self): #test normal sign up
        GenericAndroidTests.SignUp()

    def test_passintegrity(self): #attempt different password scenaraios
        GenericAndroidTests.SignUpWeakPass()

    ############################## LOG IN TESTS ###########################

    def test_login(self): #test login with an existing email
        GenericAndroidTests.Login()

    def test_wrongpass(self): #test login but insert wrong password
        GenericAndroidTests.WrongPass()

    def test_logout(self): #test logging out
        GenericAndroidTests.Logout()
        
    ############################## LIKING TESTS ###########################

    # def test_liking(self):
    #     GenericAndroidTests.LikeAnEvent()

    ############################## SEARCHING TESTS ########################

    def test_search(self): #test normal searching
        GenericAndroidTests.SearchBasic()

    def test_blanksearch(self): #test searching without a query
        GenericAndroidTests.BlankSearch()

    ############################## ORGANIZER TESTS ##########################

    def test_drafts(self): #test login with an existing email
        GenericAndroidTests.DraftsExist()

    def test_ec(self): #test login but insert wrong password
        GenericAndroidTests.CreateEvent(RandomEventName)

    def test_searchforownevent(self): #search for just published event
        GenericAndroidTests.SearchForPublishedEvent(RandomEventName)

if __name__ == "__main__":
    # unittest.main()
    with open('android_test_results.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner)