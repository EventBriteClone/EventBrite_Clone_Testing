from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import datetime
import WebsiteDriverInit

mainURL="https://www.eventbrite.com/"
loginButtonXPATH = "/html/body/div[2]/div/div[1]/div/div/header/div/div[1]/div[2]/div[2]/a[1]/span[2]"
driver = WebsiteDriverInit.init()
driver.get(mainURL)
driver.maximize_window()
usernameT=" miraaayman770@gmail.com"
passwordT="Software123?"
login = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, loginButtonXPATH))
login.click()
sleep(5)
driver.find_element(By.ID,"email").send_keys(usernameT)
input_field=driver.find_element(By.ID,"password")
input_field.send_keys(passwordT)

input_field.send_keys(Keys.RETURN)
input_field.send_keys(Keys.ENTER)
#unlike
sleep(20)
# driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/header/div/div[1]/div[2]/div[1]/a/span[1]/i/svg/path").click()
# sleep(10)
# driver.find_element(By.ID,"heart-fill-chunky_svg__eds-icon--heart-fill-chunky_base").click()
# sleep(10)
# driver.refresh()
# sleep(10)
# assert "Add events, share with friends!" in driver.page_source
# driver.close()
############
#search and likec
Searchbar=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/header/div/div[1]/div[1]/button/div/div/div/div")
Searchbar.click()
sleep(5)
searchh=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div/div/div[1]/div/div/main/div/div/div/main/header/div/form/div/div/div/div/input")
searchh.send_keys("The Design Show Egypt")
searchh.send_keys(Keys.RETURN)
# searchh.send_keys(Keys.ENTER)
sleep(10)
#like the event
HEARTt=driver.find_element(By.ID,"heart-chunky_svg__eds-icon--user-chunky_svg")
HEARTt.click()
sleep(10)
# HEARTt.click()
#unlike
sleep(10)
driver.refresh()
sleep(10)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/header/div/div[1]/div[2]/div[1]/a/span[1]/i/svg/path").click()
sleep(10)
driver.find_element(By.ID,"heart-fill-chunky_svg__eds-icon--heart-fill-chunky_base").click()
sleep(10)
driver.refresh()
sleep(10)
assert "Add events, share with friends!" in driver.page_source
driver.close()
###########
