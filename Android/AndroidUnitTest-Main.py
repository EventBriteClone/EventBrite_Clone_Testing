# import the Unit Test module
import unittest
# could be necessary (??)
import os
import sys
import time
# Global driver that the Main routine and the test files use
import AndroidDriverInit
# Import test files
import GenericAndroidTests


class EvenBriteSearch(unittest.TestCase):

    def test_SUnoAt(self): #test sign up with invalid email
        GenericAndroidTests.SignUpNoAt()
    
    def test_SU(self): #test normal sign up
        GenericAndroidTests.SignUp()

    def test_login(self): #test login with an existing email
        GenericAndroidTests.Login()

    # def test_wrongpass(self): #test login but insert wrong password
    #     GenericAndroidTests.WrongPass()

    def test_passintegrity(self): #attempt different password scenaraios
        GenericAndroidTests.SignUpWeakPass()

        
if __name__ == "__main__":
    # unittest.main()
    with open('android_test_results.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner)