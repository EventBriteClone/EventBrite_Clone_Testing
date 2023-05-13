import AndroidDriverInit
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
import time
import random
import string
from faker import Faker
from appium.webdriver.common.touch_action import TouchAction
import subprocess

def adbSendText(text):
    escaped_text = text.replace(" ", "\\ ")
    command = f"adb shell input text '{escaped_text}'"
    subprocess.run(command, shell=True)
    time.sleep(10)

def createEmail():
    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add a domain name
    email = username + '@gmail.com'
    return email,username

def createWrongEmail():
    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add a domain name
    email = username
    return email,username

###################### END OF HELPER FUNCTIONS ######################

def BasicLogin():
    global driver
    driver = AndroidDriverInit.init()
    time.sleep(10)
    action = TouchAction(driver)
    action.tap(x=700, y=2300).perform()
    time.sleep(3)
    time.sleep(5)
    byEmail = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with email address")
    byEmail.click()
    time.sleep(5)
    email = "youssss@gmail.com"
    action = TouchAction(driver)
    action.tap(x=600, y=400).perform()
    time.sleep(3)
    adbSendText(email)
    next = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next")
    next.click()
    time.sleep(5)
    

emailfield = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText"

SUEmailXpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]"
SUNameXpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]"
SULNameXpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]"
SUPassXpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[4]"
SUNextXpath = '//android.widget.Button[@content-desc="Sign Up"]'
SIPassfield = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText"

############################################### SIGN UP TESTS ##################################################

def SignUp(): #attempt log in with a never used before email (rnd)
    driver = AndroidDriverInit.init()
    time.sleep(10)
    action = TouchAction(driver)
    action.tap(x=700, y=2300).perform()
    time.sleep(3)
    time.sleep(5)
    byEmail = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with email address")
    byEmail.click()
    time.sleep(5)
    email , username = createEmail()
    action = TouchAction(driver)
    action.tap(x=600, y=400).perform()
    time.sleep(3)
    adbSendText(email)
    next = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next")
    next.click()
    time.sleep(20)
    SignUpEmailField = driver.find_element(by=AppiumBy.XPATH, value=SUEmailXpath)
    SignUpEmailField.send_keys(email)
    namefield = driver.find_element(by=AppiumBy.XPATH, value=SUNameXpath)
    lnamefield = driver.find_element(by=AppiumBy.XPATH, value=SULNameXpath)
    namefield.send_keys("John")
    lnamefield.send_keys("Smith")
    SignUpPasswordField = driver.find_element(by=AppiumBy.XPATH, value=SUPassXpath)
    SignUpPasswordField.send_keys("Qwerty123_")
    SignUpNextButton = driver.find_element(by=AppiumBy.XPATH, value=SUNextXpath)
    SignUpNextButton.click()
    time.sleep(5)
    assert "Welcome.." in driver.page_source
    driver.close()

def SignUpNoAt(): #attempt log in with an invalid email (no @ symbol)
    driver = AndroidDriverInit.init()
    time.sleep(10)
    action = TouchAction(driver)
    action.tap(x=700, y=2300).perform()
    time.sleep(3)
    byEmail = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with email address")
    byEmail.click()
    time.sleep(5)
    email , username = createWrongEmail()
    action = TouchAction(driver)
    action.tap(x=600, y=400).perform()
    time.sleep(3)
    adbSendText(email)
    next = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next")
    next.click()
    time.sleep(20)
    assert not next.is_enabled()
    driver.close()

def SignUpWeakPass(): #attempt log in with a never used before email (rnd) and passwords that don't meet the criteria
    driver = AndroidDriverInit.init()
    time.sleep(10)
    Login = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login")
    Login.click()
    time.sleep(5)
    byEmail = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with email address")
    byEmail.click()
    time.sleep(5)
    email , username = createEmail()
    action = TouchAction(driver)
    action.tap(x=600, y=400).perform()
    time.sleep(3)
    adbSendText(email)
    next = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next")
    next.click()
    time.sleep(20)
    SignUpEmailField = driver.find_element(by=AppiumBy.XPATH, value=SUEmailXpath)
    namefield = driver.find_element(by=AppiumBy.XPATH, value=SUNameXpath)
    lnamefield = driver.find_element(by=AppiumBy.XPATH, value=SULNameXpath)
    SignUpEmailField.send_keys(email)
    namefield.send_keys("John")
    lnamefield.send_keys("Smith")
    ################ PASSES #####################
    passesarray = ["qwerty", "qwertyasd", "qwerty123", "qwerty123_", "Qwerty123"]
    cond1, cond2, cond3, cond4, cond5, cond6 = False
    condarray = [cond1, cond2, cond3, cond4, cond5]
    counter = 0
    #############################################

    SignUpPasswordField = driver.find_element(by=AppiumBy.XPATH, value=SUPassXpath)
    SignUpNextButton = driver.find_element(by=AppiumBy.XPATH, value=SUNextXpath)

    for i in passesarray:
        SignUpPasswordField.send_keys(i)
        condarray[counter] = not SignUpNextButton.is_enabled()
        counter+=1
        for i in range(len(i)):
            SignUpPasswordField.send_keys(Keys.BACK_SPACE)

    SignUpPasswordField.send_keys("Qwerty123_")
    cond6 = SignUpNextButton.is_enabled()
    if cond1 == cond2 == cond3 == cond4 == cond5 == cond6 == True:
        assert True
    else:
        assert False
    driver.close()

############################################### LOG IN TESTS ##################################################

def Login(): #attempt log in with a signed up email
    BasicLogin()
    password = "Yusuy_2000"
    action = TouchAction(driver)
    action.tap(x=700, y=975).perform()
    time.sleep(3)
    adbSendText(password)
    LoginButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login")
    LoginButton.click()
    time.sleep(10)
    assert "Welcome.." in driver.page_source
    driver.close()

def WrongPass(): #attempt login with a signed up email but use wrong password
    BasicLogin()
    password = "Wrong_pass123"
    action = TouchAction(driver)
    action.tap(x=700, y=975).perform()
    time.sleep(3)
    adbSendText(password)
    time.sleep(5)
    LoginButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login")
    LoginButton.click()
    time.sleep(5)
    assert "Password is not correct" in driver.page_source
    driver.close()

def Logout():
    BasicLogin()
    password = "Yusuy_2000"
    action = TouchAction(driver)
    action.tap(x=700, y=975).perform()
    time.sleep(3)
    adbSendText(password)
    LoginButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login")
    LoginButton.click()
    time.sleep(10)
    AttendeeButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Attendee")
    AttendeeButton.click()
    time.sleep(10)
    AccSettings = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tab 5 of 5")
    AccSettings.click()
    time.sleep(5)
    LogoutButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Log out")
    LogoutButton.click()
    assert "Log in" in driver.page_source

############################################### LIKING TESTS ##################################################

def LikeAnEvent(): #HMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    password = "Yusuy_2000"
    action = TouchAction(driver)
    action.tap(x=700, y=975).perform()
    time.sleep(3)
    adbSendText(password)
    LoginButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login")
    LoginButton.click()
    time.sleep(10)
    AttendeeButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Attendee")
    AttendeeButton.click()
    time.sleep(10)
    SampleEvent = driver.find_element(by=AppiumBy.XPATH, value="")
    SampleEvent.click()
    driver.close()

############################################### SEARCHING TESTS ################################################

def SearchBasic():
    BasicLogin()
    password = "Yusuy_2000"
    action = TouchAction(driver)
    action.tap(x=700, y=975).perform()
    time.sleep(3)
    adbSendText(password)
    LoginButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login")
    LoginButton.click()
    time.sleep(10)
    AttendeeButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Attendee")
    AttendeeButton.click()
    time.sleep(10)
    SearchButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tab 2 of 5")
    SearchButton.click()
    time.sleep(5)
    SearchBar = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText")
    SearchBar.send_keys("gg")
    SearchIcon = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button")
    SearchIcon.click()
    assert "Results for: gg" in driver.page_source
    time.sleep(15)
    
def BlankSearch():
    BasicLogin()
    password = "Yusuy_2000"
    action = TouchAction(driver)
    action.tap(x=700, y=975).perform()
    time.sleep(3)
    adbSendText(password)
    LoginButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login")
    LoginButton.click()
    time.sleep(10)
    AttendeeButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Attendee")
    AttendeeButton.click()
    time.sleep(10)
    SearchButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tab 2 of 5")
    SearchButton.click()
    time.sleep(5)
    SearchIcon = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button")
    SearchIcon.click()
    assert "Please enter a valid value" in driver.page_source
    time.sleep(15)

################################################### ORGANIZER TESTS ################################################

def DraftsExist():
    BasicLogin()
    password = "Yusuy_2000"
    action = TouchAction(driver)
    action.tap(x=700, y=975).perform()
    time.sleep(3)
    adbSendText(password)
    time.sleep(10)
    OrgButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Organizer")
    OrgButton.click()
    time.sleep(10)
    Drafts = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Draft\nTab 3 of 3")
    Drafts.click()
    time.sleep(5)
    assert "Locust" in driver.page_source
    driver.close()
 
def CreateEvent(x):
    password = "Yusuy_2000"
    action = TouchAction(driver)
    action.tap(x=700, y=975).perform()
    time.sleep(3)
    adbSendText(password)
    time.sleep(10)
    OrgButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Organizer")
    OrgButton.click()
    time.sleep(10)
    PlusButton = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[2]")
    PlusButton.click()
    EventTitle = driver.find_element(by=AppiumBy.XPATH, value="insert value here")
    EventTitle.send_keys(x)
    Venue = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Venue")
    Venue.click()
    time.sleep(3)
    Online = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Online Event")
    Online.click()
    time.sleep(5)
    NextButton = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button")
    NextButton.click()
    time.sleep(5)
    Save = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Save")
    Save.click()
    HamburgerMenu = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[1]")
    HamburgerMenu.click()
    time.sleep(3)
    Publish = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Publish")
    Publish.click()
    time.sleep(5)
    next = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next")
    next.click()
    time.sleep(10)
    assert "Successfully" in driver.page_source
    driver.close()

def SearchForPublishedEvent(x):
    BasicLogin()
    password = "Yusuy_2000"
    action = TouchAction(driver)
    action.tap(x=700, y=975).perform()
    time.sleep(3)
    adbSendText(password)
    LoginButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login")
    LoginButton.click()
    time.sleep(10)
    AttendeeButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Attendee")
    AttendeeButton.click()
    time.sleep(10)
    SearchButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tab 2 of 5")
    SearchButton.click()
    time.sleep(5)
    SearchBar = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText")
    SearchBar.send_keys(x)
    SearchIcon = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button")
    SearchIcon.click()
    assert "Online Event" in driver.page_source
    time.sleep(15)
