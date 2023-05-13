from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import WebsiteDriverInit
import Names
righttagarray = []
longtagarray = []
shorttagarray = []
for i in range(10):
    righttagarray.append("tag"+str(i))
for i in range(11):
    longtagarray.append("tag"+str(i))
for i in range(9):
    shorttagarray.append("tag"+str(i))

def LoginAndStartCreating():
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
    Create = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.CreateEventbuttoum))
    Create.click()
    sleep(5)

def TheNormalEventCreation():
    LoginAndStartCreating()
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.EventNameSpace))
    name.send_keys("Sample Name")
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.EventDescription))
    name.send_keys("Sample Name")
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.EventTitle))
    name.send_keys("Sample Name")
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.Organizer))
    name.send_keys("Sample Name")
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.Tags))
    name.send_keys("Sample Name")
    sleep(10)
    # Addd = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.AddTagButton))
    # sleep(3)
    # Addd.click()
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.VenueSpace))
    name.send_keys("Sample Venue")
    Create = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.SaveContinueButton))
    Create.click()
    sleep(15)
    # assert "Publish Your Event" in driver.page_source
    # driver.close()
def NormalEventCreation():
    TheNormalEventCreation()
    assert "Publish Your Event" in driver.page_source
    driver.close()    
def PublishEvent():
    TheNormalEventCreation()
    Publish = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.PuplishEventXpath))
    Publish.click()
    sleep(30)
    assert "Let's create tickets" in driver.page_source
    driver.close()



def NoLocation():
    LoginAndStartCreating()
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.EventNameSpace))
    name.send_keys("Sample Name")
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.EventDescription))
    name.send_keys("Sample Name")
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.EventTitle))
    name.send_keys("Sample Name")
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.Organizer))
    name.send_keys("Sample Name")
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.Tags))
    name.send_keys("Sample Name")
    sleep(15)
    Create = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.SaveContinueButton))
    Create.click()
    sleep(15)
    assert "Location is required." in driver.page_source
    driver.close()

def NoTitle():
    LoginAndStartCreating()
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.EventNameSpace))
    name.send_keys("Sample Name")
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.EventDescription))
    name.send_keys("Sample Name")
    sleep(15)
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.EventTitle))
    name.send_keys(Keys.RETURN)
    sleep(15)
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.Organizer))
    name.send_keys("Sample Name")
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.Tags))
    name.send_keys("Sample Name")
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.VenueSpace))
    name.send_keys("Sample Venue")
    Create = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.SaveContinueButton))
    Create.click()
    sleep(15)
    assert "This is required." in driver.page_source
    driver.close()