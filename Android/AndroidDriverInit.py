from appium import webdriver

# Appium driver initialization

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.example.event_brite_app',
    appActivity='.MainActivity',
    language='en',
    locale='US'
)
appium_server_url = 'http://localhost:4723'
def init():
    driver = webdriver.Remote(appium_server_url, capabilities)
    return driver