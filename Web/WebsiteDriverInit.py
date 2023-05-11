from selenium import webdriver

# Selenium driver initialization
def init():
    path = r"C:\Users\youss\Desktop\SWE\msedgedriver.exe"
    driver = webdriver.Edge()
    return driver


