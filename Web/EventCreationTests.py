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

loginButtonXPATH = "/html/body/div[2]/div/div[1]/div/div/header/div/div[1]/div[2]/div[2]/a[1]/span[2]"
CreateEventXPATH = "/html/body/div[2]/div/div[1]/div/div/header/div/div[1]/div[2]/a"
TypeSelector = "#eventType"
CategorySelector = "#eventSubTopic"
EventNameSelector = "#event-basicInfo-title"
OrganizerSelector = "#event-basicinfo-create-organizer-profile"
TagFieldSelector = "#tagging-form-field"
AddTagButtonClass = "eds-btn eds-btn--button eds-btn--neutral eds-btn--responsive"
VenueSelector = "#event-locationautocomplete-location"
SaveButtonXPATH = "/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/button[2]"
OnlineVenueXPATH = "/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/label"


def LoginAndStartCreating():
    global driver 
    driver = WebsiteDriverInit.init()
    usernameT=" miraaayman770@gmail.com"
    passwordT="Software123?"
    mainURL="https://www.event-us.me/"
    driver.get(mainURL)
    driver.maximize_window()
    sleep(5)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, loginButtonXPATH))
    login.click()
    sleep(5)
    driver.find_element(By.ID,"email").send_keys(usernameT)
    input_field=driver.find_element(By.ID,"password")
    input_field.send_keys(passwordT)
    sleep(5)
    input_field.send_keys(Keys.RETURN)
    sleep(10)
    Create = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, CreateEventXPATH))
    Create.click()
    sleep(5)

def NormalEventCreation():
    LoginAndStartCreating()
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.CSS_SELECTOR, EventNameSelector))
    name.send_keys("Sample Name")
    venue = driver.find_element(By.XPATH, OnlineVenueXPATH)
    venue.click()
    sleep(5)
    savebutton = driver.find_element(By.XPATH, SaveButtonXPATH)
    savebutton.click()
    sleep(10)
    assert "Preview Your Event" in driver.page_source
    driver.close()

def TestTagLimit():
    LoginAndStartCreating()

    TagBox = driver.find_element(By.CSS_SELECTOR, TagFieldSelector)
    for i in longtagarray:
        TagBox.click()
        TagBox.send_keys(i)
        TagBox.send_keys(Keys.RETURN)
        sleep(1)
    assert "10/10 tag limit reached." in driver.page_source
    driver.close()

def TestDoubleTags():
    LoginAndStartCreating()
    TagBox = driver.find_element(By.CSS_SELECTOR, TagFieldSelector)
    for i in shorttagarray:
        TagBox.click()
        TagBox.send_keys(i)
        TagBox.send_keys(Keys.RETURN)
        sleep(1)
    TagBox.send_keys(shorttagarray[0])
    assert "Tag already exists." in driver.page_source
    driver.close()

def NoLocation():
    LoginAndStartCreating()
    name = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.CSS_SELECTOR, EventNameSelector))
    name.send_keys("Sample Name")
    savebutton = driver.find_element(By.XPATH, SaveButtonXPATH)
    savebutton.click()
    sleep(2)
    assert "Location is required" in driver.page_source
    driver.close()

def NoTitle():
    LoginAndStartCreating()
    TagBox = driver.find_element(By.CSS_SELECTOR, TagFieldSelector)
    TagBox.send_keys("Randomnessssss")
    sleep(3)
    savebutton = driver.find_element(By.XPATH, SaveButtonXPATH)
    savebutton.click()
    sleep(2)
    assert "Title is required." in driver.page_source
    driver.close()