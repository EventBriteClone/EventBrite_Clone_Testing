from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import WebsiteDriverInit
import Names 
def LoginAndStart():
    global driver 
    driver = WebsiteDriverInit.init()
    usernameT="ziad@gmail.com"
    passwordT="512002ziad"
    mainURL="https://www.event-us.me/"
    driver.get(mainURL)
    driver.maximize_window()
    sleep(5)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.loginButton))
    login.click()
    sleep(5)
    driver.find_element(By.ID,"email").send_keys(usernameT)
    input_field=driver.find_element(By.ID,"password")
    input_field.send_keys(passwordT)
    sleep(5)
    input_field.send_keys(Keys.RETURN)
    sleep(10)
    Create = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.DropDownUserMenue))
    Create.click()
    sleep(5)
def Logout():
    LoginAndStart()
    sleep(5)
    # Menuu = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.DropDownUserMenue))
    # # action = ActionChains(driver)

    # # # Perform mouse hover on the element
    # # action.move_to_element(login).perform()
    # # login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.DropDownUserMenue))
    # Menuu.click()
    # sleep(10)
    logout = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.LogOutButton))
    logout.click()
    sleep(10)
    assert   "Log In" in driver.page_source
    driver.close()