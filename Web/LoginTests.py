from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import WebsiteDriverInit

loginButtonXPATH = "/html/body/div[2]/div/div[1]/div/div/header/div/div[1]/div[2]/div[2]/a[1]/span[2]"

def NormalLogin():
    driver = WebsiteDriverInit.init()
    username="mohra_ayman@gmail.com"
    usernameT=" miraaayman770@gmail.com"
    passwordT="Software123?"
    password="565t5yG4rrtghj"
    loginurl="https://www.eventbrite.com/signin/?referrer=%2F"
    mainURL="https://www.eventbrite.com/"
    driver.get(mainURL)
    # driver.maximize_window()
    sleep(5)
    login  = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, loginButtonXPATH))
    login.click()
    sleep(5)
    driver.find_element(By.ID,"email").send_keys(usernameT)
    input_field=driver.find_element(By.ID,"password")
    input_field.send_keys(passwordT)
    sleep(5)
    input_field.send_keys(Keys.RETURN)
    sleep(10)
    assert "Miraa" in driver.page_source
    driver.close()

def TestLoginWrongEmail():
    driver = WebsiteDriverInit.init()
    username=" miraaayman70@gmail.com"
    password="Software123?"
    driver.get("https://www.eventbrite.com/")
    # driver.maximize_window()
    sleep(5)
    login  = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, loginButtonXPATH))
    login.click()
    sleep(5)
    driver.find_element(By.ID,"email").send_keys(username)
    input_field=driver.find_element(By.ID,"password")
    input_field.send_keys(password)
    sleep(5)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    assert "There is no account associated with the email." in driver.page_source
    driver.close()

def BlankLogin():
    driver = WebsiteDriverInit.init()
    driver.get("https://www.eventbrite.com/")
    sleep(5)
    login  = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, loginButtonXPATH))
    login.click()
    input_field=driver.find_element(By.ID,"password")
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    assert "Password is required" in driver.page_source
    driver.close()







