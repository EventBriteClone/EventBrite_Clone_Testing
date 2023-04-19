from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import WebsiteDriverInit
import Names 
def NormalLogin():
    driver = WebsiteDriverInit.init()
    usernameT=" miraaayman770@gmail.com"
    passwordT="Software123?"
    usernameT="ziad@gmail.com"
    passwordT="512002ziad"
    mainURL="https://www.event-us.me/"
    driver.get(mainURL)
    sleep(5)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, Names.loginButtonXPATH))
    login.click()
    sleep(5)
    driver.find_element(By.XPATH,Names.EmailSpace).send_keys(usernameT)
    sleep(15)

    input_field=driver.find_element(By.XPATH,Names.PaswordSpace)
    input_field.send_keys(passwordT)
    sleep(5)
    input_field.send_keys(Keys.RETURN)
    sleep(10)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.loginConfirmButton))
    login.click()  
    assert "ziad" in driver.page_source
    driver.close()

def TestLoginWrongEmail():
    driver = WebsiteDriverInit.init()
    username=" miraaayman70@gmail.com"
    password="Software123?"
    driver.get("https://www.event-us.me/")
    # driver.maximize_window()
    sleep(5)
    login  = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, Names.loginButtonXPATH))
    login.click()
    sleep(5)
    driver.find_element(By.XPATH,Names.EmailSpace).send_keys(username)
    input_field=driver.find_element(By.XPATH,Names.PaswordSpace)
    input_field.send_keys(password)
    sleep(5)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.loginConfirmButton))
    login.click()
    assert "There is no account associated with the email." in driver.page_source
    driver.close()

def TestLoginWrongPassword():
    driver = WebsiteDriverInit.init()
    username=" miraaayman770@gmail.com"
    username="ziad@gmail.com"
    password="oftSware1255"
    password="512002ziad"
    driver.get("https://www.event-us.me/")
    # driver.maximize_window()
    sleep(5)
    login  = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, Names.loginButtonXPATH))
    login.click()
    sleep(5)
    driver.find_element(By.XPATH,Names.EmailSpace).send_keys(username)
    input_field=driver.find_element(By.XPATH,Names.PaswordSpace)
    input_field.send_keys(password)
    sleep(5)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.loginConfirmButton))
    login.click()
    assert "The password is not correct." in driver.page_source
    driver.close()

def TestBlankLogin():
    driver = WebsiteDriverInit.init()
    driver.get("https://www.event-us.me/")
    sleep(5)
    login  = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, Names.loginButtonXPATH))
    login.click()
    sleep(5)
    driver.find_element(By.XPATH,Names.EmailSpace).send_keys(Keys.RETURN)
    input_field=driver.find_element(By.ID,"password")
    input_field.send_keys(Keys.RETURN)
    sleep(30)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.loginConfirmButton))
    login.click() 
    assert "Please enter a valid email address" in driver.page_source
    driver.close()

def TestBlankPasswordLogin():
    driver = WebsiteDriverInit.init()
    username=" miraaayman770@gmail.com"
    driver.get("https://www.event-us.me/")
    sleep(5)
    login  = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, Names.loginButtonXPATH))
    login.click()
    sleep(5)
    driver.find_element(By.XPATH,Names.EmailSpace).send_keys(username)
    input_field=driver.find_element(By.ID,"password")
    input_field.send_keys(Keys.RETURN)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.loginConfirmButton))
    login.click() 
    sleep(5)
    assert "Password is required" in driver.page_source
    driver.close()    
