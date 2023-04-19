import AndroidDriverInit
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
import time
import random
import string
from faker import Faker

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

def NormalLogin():
    global driver
    driver = AndroidDriverInit.init()
    time.sleep(10)
    Favs = driver.find_element(by=AppiumBy.XPATH, value=FavsPath)
    Favs.click()
    time.sleep(10)
    Login = driver.find_element(by=AppiumBy.XPATH, value=LoginPath)
    Login.click()
    time.sleep(5)
    byEmail = driver.find_element(by=AppiumBy.XPATH, value=byEmailPath)
    byEmail.click()
    time.sleep(5)
    field = driver.find_element(by=AppiumBy.XPATH, value=emailfield)
    email = "take email from Youssef Saad"
    field.send_keys(email)
    next = driver.find_element(by=AppiumBy.XPATH, value=NextPath)
    next.click()
    time.sleep(20)

emailfield = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText"
FavsPath = '//android.view.View[@content-desc="Tab 3 of 5"]'
LoginPath = '//android.view.View[@content-desc="Log in"]'
byEmailPath = '//android.view.View[@content-desc="Continue with email address"]'
NextPath = '//android.widget.Button[@content-desc="Next"]'

# def SampleTest():
#     driver = AndroidDriverInit.init()
#     time.sleep(10)
#     el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Tab 2 of 5"]')
#     el.click()
#     time.sleep(10)
#     assert "Allow event_brite_app to access this device’s location?" in driver.page_source
#     driver.close()

def SignUp(): #attempt log in with a never used before email (rnd)
    driver = AndroidDriverInit.init()
    time.sleep(10)
    Favs = driver.find_element(by=AppiumBy.XPATH, value=FavsPath)
    Favs.click()
    time.sleep(10)
    Login = driver.find_element(by=AppiumBy.XPATH, value=LoginPath)
    Login.click()
    time.sleep(5)
    byEmail = driver.find_element(by=AppiumBy.XPATH, value=byEmailPath)
    byEmail.click()
    time.sleep(5)
    field = driver.find_element(by=AppiumBy.XPATH, value=emailfield)
    email , username = createEmail()
    field.send_keys(email)
    next = driver.find_element(by=AppiumBy.XPATH, value=NextPath)
    next.click()
    time.sleep(20)
    assert "[insert haga hena]" in driver.page_source
    driver.close()

def SignUpNoAt(): #attempt log in with an invalid email (no @ symbol)
    driver = AndroidDriverInit.init()
    time.sleep(10)
    Favs = driver.find_element(by=AppiumBy.XPATH, value=FavsPath)
    Favs.click()
    time.sleep(10)
    Login = driver.find_element(by=AppiumBy.XPATH, value=LoginPath)
    Login.click()
    time.sleep(5)
    byEmail = driver.find_element(by=AppiumBy.XPATH, value=byEmailPath)
    byEmail.click()
    time.sleep(5)
    field = driver.find_element(by=AppiumBy.XPATH, value=emailfield)
    email , username = createWrongEmail()
    field.send_keys(email)
    next = driver.find_element(by=AppiumBy.XPATH, value=NextPath)
    next.click()
    time.sleep(20)
    if next.is_enabled():
        assert True
    else:
        assert False
    driver.close()

def SignUpWeakPass(): #attempt log in with a never used before email (rnd)
    driver = AndroidDriverInit.init()
    time.sleep(10)
    Favs = driver.find_element(by=AppiumBy.XPATH, value=FavsPath)
    Favs.click()
    time.sleep(10)
    Login = driver.find_element(by=AppiumBy.XPATH, value=LoginPath)
    Login.click()
    time.sleep(5)
    byEmail = driver.find_element(by=AppiumBy.XPATH, value=byEmailPath)
    byEmail.click()
    time.sleep(5)
    field = driver.find_element(by=AppiumBy.XPATH, value=emailfield)
    email , username = createEmail()
    field.send_keys(email)
    next = driver.find_element(by=AppiumBy.XPATH, value=NextPath)
    next.click()
    time.sleep(20)
    ################ PASSES #####################
    passesarray = ["qwerty", "qwertyasd", "qwerty123", "qwerty123_", "Qwerty123_"]
    cond1, cond2, cond3, cond4, cond5 = False
    condarray = [cond1, cond2, cond3, cond4, cond5]
    counter = 0
    #############################################
    passfield = driver.find_element(by=AppiumBy.XPATH, value="passfield")
    nextbutton = driver.find_element(by=AppiumBy.XPATH, value="nextbutton")
    for i in passesarray:
        passfield.send_keys(i)
        condarray[counter] = not nextbutton.is_enabled()
        counter+=1
        for i in range(len(i)):
            passfield.send_keys(Keys.BACK_SPACE)
    if cond1 == cond2 == cond3 == cond4 == cond5 == True:
        assert True
    else:
        assert False
    driver.close()

def Login(): #attempt log in with a signed up email
    NormalLogin()
    assert "[insert haga hena]" in driver.page_source
    driver.close()

def WrongPass(): #attempt login with a signed up email but use wrong password
    NormalLogin()
    PasswordField = driver.find_element(by=AppiumBy.XPATH, value=byEmailPath)
    PasswordField.send_keys("wrong_password123")
    time.sleep(5)
    #Need element for next button!!!!!!!!!!!!!!!!!
    assert "The password you entered is incorrenct" in driver.page_source
    driver.close()