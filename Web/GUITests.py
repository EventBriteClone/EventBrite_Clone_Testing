from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import WebsiteDriverInit
import Names 
mainURL="https://www.event-us.me/"
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
# def GUI():
#     LoginAndStart()
#     sleep(5)
#     Tickets()
#     ItIsMyAccount()

# # Assert the expected page
#     assert 'new-page-url' in driver.current_url

def Likes():
    LoginAndStart()
    Likess = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.LikesButton))
    Likess.click()
    # WebDriverWait(driver, 10).until(EC.url_changes(mainURL))

    # Assert that the URL has changed
    assert "Add events, share with friends" in driver.page_source
    driver.close()
def ManageEventsTest():
    LoginAndStart()
    ManageEvents = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.ManageEventsButton))
    ManageEvents.click()
    # WebDriverWait(driver, 10).until(EC.url_changes(mainURL))

    # Assert that the URL has changed
    assert "List" in driver.page_source
    driver.close()
# def BrowesEventTest():
#     LoginAndStart()
#     BrowesEventt = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.BrowesEvent))
#     BrowesEventt.click()
#     # WebDriverWait(driver, 10).until(EC.url_changes(mainURL))

#     # Assert that the URL has changed
#     assert driver.current_url != mainURL
def ItIsMyAccount():
    LoginAndStart()
    sleep(10)
    ManageEvents = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.ManageEventsButton))
    ManageEvents.click()
    assert "ziad" in driver.page_source
    driver.close()
