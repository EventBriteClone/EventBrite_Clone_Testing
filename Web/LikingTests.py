from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import datetime

mainURL="https://www.eventbrite.com/"
path = r"C:\Users\youss\Desktop\SWE\msedgedriver.exe"
loginButtonXPATH = "/html/body/div[2]/div/div[1]/div/div/header/div/div[1]/div[2]/div[2]/a[1]/span[2]"

driver = webdriver.Edge()
driver.get(mainURL)

driver.maximize_window()
# driver = WebsiteDriverInit.init()
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

# driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/section/div/main/div/main/div[1]/div/div/div/div/div/div/article/div[3]/div/span[2]/span/button/i/svg/path").click()
# sleep(10)
# input=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/input")
# input.send_keys("Cairo")
# input.send_keys(Keys.RETURN)
# input.send_keys(Keys.ENTER)
# driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/ul/li[1]/div/button/div/div/div[1]").click()
# sleep(20)
# driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/div/div/div/section[1]/div/div/div[2]/div[1]/div/div/article/div[1]/div[3]/span/span/button/i/svg").click()

# search_box=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/header/div/div[1]/div[1]/button/div/div/div/div")
# search_box.click()

# sleep(10)
# # search_box=driver.find_element(By.ID,"global-header")
# # search_box.click()

# sleep(10)
# driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div/div/div[1]/div/div/main/div/div/div/main/header/div/ul/li[2]/div/span").click()
# sleep(10)
# search_box=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/div/div/section[1]/div/header/form/nav/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div/input")
# sleep(10)
# search_box.send_keys("Egypt")
# search_box.send_keys(Keys.RETURN)
# search_box.send_keys(Keys.ENTER)
# driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/div/div/section[1]/div/header/form/nav/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/ul/li[1]/div/button/div/div/div[1]").click()
# sleep(5)
# page_source = driver.page_source
# word_count = page_source.count("Today")

# # Print the word count
# print(f"The word 'Today' appears {word_count} times on the webpage.")
# search_results=(driver.find_elements(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/div/div/section[1]/div/section"))
# sleep(10)
# second=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/div/div/section[1]/div/div/div/section/ul/li[1]/div/div[1]/div/div/div")
# second.click()
# # print("second",second)
# print(second("Alice"))
# text = second.text()
# sleep(20)
# # search for the word 'example' in the text
# if 'Today' in text:
#     print('The word "example" was found on the page!')
# else:
#     print('The word "example" was not found on the page.')

# num_results = len(search_results)
# print("Number of search results:", num_results)
# print("search_results",search_results)

# assert "Today" in driver.page_source