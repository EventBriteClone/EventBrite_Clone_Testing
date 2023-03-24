from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import WebsiteDriverInit
import random
import string
from faker import Faker

signupButtonXPATH="/html/body/div[2]/div/div[1]/div/div/header/div/div[1]/div[2]/div[2]/a[2]/span[2]"

def NormalSignUp():
    driver = WebsiteDriverInit.init()
    faker = Faker()
    # Generate a random first name
    first_name = faker.first_name()
    # Generate a random last name
    last_name = faker.last_name()
    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add a domain name
    email = username + '@gmail.com'
    char_set = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(char_set) for i in range(12))
    # driver.maximize_window()
    mainURL="https://www.eventbrite.com/"
    driver.get(mainURL)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, signupButtonXPATH))
    login.click()
    sleep(5)
    input_field=driver.find_element(By.ID,"email")
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    driver.find_element(By.ID,"emailConfirmation").send_keys(email)
    driver.find_element(By.ID,"firstName").send_keys(first_name)
    driver.find_element(By.ID,"lastName").send_keys(last_name)
    driver.find_element(By.ID,"password").send_keys(password)
    input_field=driver.find_element(By.XPATH ,"/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[3]/div/button")
    input_field.click()
    sleep(5)
    driver.find_element(By.XPATH ,"/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/main/div/div/div/div/div/div[2]/button[2]").click()
    sleep(20)
    assert username in driver.page_source
    driver.close()

def testSignUpWrongNames():
    driver = WebsiteDriverInit.init()
    faker = Faker()
    # Generate a random first name
    first_name = six_digit_number = random.randint(100000, 999999)

    # Generate a random last name
    last_name = six_digit_number = random.randint(100000, 999999)

    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add a domain name
    email = username + '@gmail.com'
    char_set = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(char_set) for i in range(12))
    # driver.maximize_window()
    mainURL="https://www.eventbrite.com/"
    driver.get(mainURL)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, signupButtonXPATH))
    login.click()
    sleep(5)
    input_field=driver.find_element(By.ID,"email")
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    driver.find_element(By.ID,"emailConfirmation").send_keys(email)
    driver.find_element(By.ID,"firstName").send_keys(first_name)
    driver.find_element(By.ID,"lastName").send_keys(last_name)
    driver.find_element(By.ID,"password").send_keys(password)
    input_field=driver.find_element(By.XPATH ,"/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[3]/div/button")
    input_field.click()
    sleep(5)
    driver.find_element(By.XPATH ,"/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/main/div/div/div/div/div/div[2]/button[2]").click()
    sleep(20)
    assert username in driver.page_source
    driver.close()    

def testSignUpWrongEmailDomian():
    driver = WebsiteDriverInit.init()
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add a domain name
    email = username + '@karam'
    mainURL="https://www.eventbrite.com/"
    driver.get(mainURL)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, signupButtonXPATH))
    login.click()
    sleep(5)
    input_field=driver.find_element(By.ID,"email")
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    assert "Invalid email" in driver.page_source
    driver.close()

def testSignUpWrongEmail():
    driver = WebsiteDriverInit.init()
    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add a domain name
    email = username 
    mainURL="https://www.eventbrite.com/"
    driver.get(mainURL)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, signupButtonXPATH))
    login.click()
    sleep(5)
    input_field=driver.find_element(By.ID,"email")
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(3)
    assert "Please include an '@' in the email address" in driver.page_source
    # driver.find_element(By.ID,"emailConfirmation").send_keys(email)
    # driver.find_element(By.ID,"firstName").send_keys(first_name)
    # driver.find_element(By.ID,"lastName").send_keys(last_name)
    # driver.find_element(By.ID,"password").send_keys(password)
    # input_field=driver.find_element(By.XPATH ,"/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[3]/div/button")
    # input_field.click()
    # sleep(5)
    # driver.find_element(By.XPATH ,"/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/main/div/div/div/div/div/div[2]/button[2]").click()
    # sleep(30)
    # assert "Please include an @" in driver.page_source
    driver.close()    

def testSignUpEmptyEmail():
    driver = WebsiteDriverInit.init()
    mainURL="https://www.eventbrite.com/"
    driver.get(mainURL)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, signupButtonXPATH))
    login.click()
    sleep(5)
    input_field=driver.find_element(By.ID,"email")
    input_field.send_keys(Keys.RETURN)
    sleep(3)
    assert "Field required" in driver.page_source
    driver.close()

def testSignUpAssociatedEmail():
    driver = WebsiteDriverInit.init()
    mainURL="https://www.eventbrite.com/"
    driver.get(mainURL)
    usernameT=" miraaayman770@gmail.com"
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, signupButtonXPATH))
    login.click()
    sleep(5)
    input_field=driver.find_element(By.ID,"email")
    input_field.send_keys(usernameT)
    input_field.send_keys(Keys.RETURN)
    sleep(3)
    assert "There is an account associated with the email." in driver.page_source
    driver.close()
    
def testSignUpDiffrentEmails():
    driver = WebsiteDriverInit.init()
    faker = Faker()
    # Generate a random first name
    first_name = faker.first_name()
    # Generate a random last name
    last_name = faker.last_name()
    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add a domain name
    email = username + '@gmail.com'
    char_set = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(char_set) for i in range(12))
    # driver.maximize_window()
    mainURL="https://www.eventbrite.com/"
    driver.get(mainURL)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, signupButtonXPATH))
    login.click()
    sleep(5)
    input_field=driver.find_element(By.ID,"email")
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add a domain name
    email = username + '@gmail.com'
    driver.find_element(By.ID,"emailConfirmation").send_keys(email)
    driver.find_element(By.ID,"firstName").send_keys(first_name)
    driver.find_element(By.ID,"lastName").send_keys(last_name)
    driver.find_element(By.ID,"password").send_keys(password)
    input_field=driver.find_element(By.XPATH ,"/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[3]/div/button")
    input_field.click()
    sleep(5)
    # driver.find_element(By.XPATH ,"/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/main/div/div/div/div/div/div[2]/button[2]").click()
    # sleep(20)
    assert "Email address doesn't match. Please try again" in driver.page_source
    driver.close()

def testSignUpWithoutFirstName():
    driver = WebsiteDriverInit.init()
    faker = Faker()
    # Generate a random last name
    last_name = faker.last_name()
    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add a domain name
    email = username + '@gmail.com'
    char_set = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(char_set) for i in range(12))
    # driver.maximize_window()
    mainURL="https://www.eventbrite.com/"
    driver.get(mainURL)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, signupButtonXPATH))
    login.click()
    sleep(5)
    input_field=driver.find_element(By.ID,"email")
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    driver.find_element(By.ID,"emailConfirmation").send_keys(email)
    driver.find_element(By.ID,"lastName").send_keys(last_name)
    driver.find_element(By.ID,"password").send_keys(password)
    input_field=driver.find_element(By.XPATH ,"/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[3]/div/button")
    input_field.click()
    sleep(5)
    # driver.find_element(By.XPATH ,"/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/main/div/div/div/div/div/div[2]/button[2]").click()
    # sleep(20)
    assert "First name is required" in driver.page_source
    driver.close()


