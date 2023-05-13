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
import Names
# Utility functions
def FirstLastName():
    faker = Faker()
    # Generate a random first name
    first_name = faker.first_name()
    # Generate a random last name
    last_name = faker.last_name()
    return first_name,last_name
def createEmail():
    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add a domain name
    email = username + '@gmail.com'
    return email,username
def ceatePasword():
    char_set = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(char_set) for i in range(12))
    return password
def createWeakPassword():
    char_set = string.digits
    # Generate a random password of the specified length
    password = ''.join(random.choice(char_set) for _ in range(8))
    return password
def fill(driver,email,first_name,last_name,password):
    driver.find_element(By.ID,Names.sigupConfirmEmailSpace).send_keys(email)
    driver.find_element(By.ID,Names.sigupFNameSpace).send_keys(first_name)
    driver.find_element(By.ID,Names.sigupLNameSpace).send_keys(last_name)
    driver.find_element(By.ID,Names.sigupPasswordSpace).send_keys(password)

# Predefined selectors
# signupButtonXPATH="/html/body/div[2]/div/div[1]/div/div/header/div/div[1]/div[2]/div[2]/a[2]/span[2]"
# AgreeButtonXPATH="/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/main/div/div/div/div/div/div[2]/button[2]"
mainURL="https://www.event-us.me/"

def NormalSignUp():
    # Initialize the web driver
    driver = WebsiteDriverInit.init()
    # Get the first name and last name
    first_name, last_name = FirstLastName()
    # Create an email and username
    email, username = createEmail()
    # Create a password
    password = ceatePasword()
    # Navigate to the website and click the signup button
    driver.get(mainURL)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.signupButton))
    login.click()
    sleep(5)
    # Fill in the email field and submit
    input_field = driver.find_element(By.ID, Names.sigupEmailSpace)
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    # Fill in the form with user details
    fill(driver, email, first_name, last_name, password)
    # Click the confirm button
    input_field = driver.find_element(By.ID, Names.ConfirmButtonXPATH)
    input_field.click()
    sleep(5)
    # Agree to the terms and conditions
    # driver.find_element(By.XPATH, AgreeButtonXPATH).click()
    # sleep(20)
    # Check if the username is present in the page source
    assert "Log in" in driver.page_source
    # Close the driver
    driver.close()

def WeackPasswordSignUp():
    # Initialize the web driver
    driver = WebsiteDriverInit.init()
    # Get the first name and last name
    first_name, last_name = FirstLastName()
    # Create an email and username
    email, username = createEmail()
    # Create a password
    password = createWeakPassword()
    # Navigate to the website and click the signup button
    driver.get(mainURL)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, Names.signupButton))
    login.click()
    sleep(5)
    # Fill in the email field and submit
    input_field = driver.find_element(By.ID, Names.sigupEmailSpace)
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    # Fill in the form with user details
    fill(driver, email, first_name, last_name, password)
    # Click the confirm button
    input_field = driver.find_element(By.ID, Names.ConfirmButtonXPATH)
    input_field.click()
    sleep(5)
    # Agree to the terms and conditions
    # driver.find_element(By.XPATH, AgreeButtonXPATH).click()
    # sleep(20)
    # Check if the username is present in the page source
    assert "Please enter a valid password" in driver.page_source
    # Close the driver
    driver.close()

def testSignUpWrongNames():
    # Initialize the web driver
    driver = WebsiteDriverInit.init()
    # Generate a random first name
    first_name = random.randint(100000, 999999)
    # Generate a random last name
    last_name = random.randint(100000, 999999)
    # Create an email and username
    email, username = createEmail()
    # Create a password
    password = ceatePasword()
    # Navigate to the website and click the signup button
    driver.get(mainURL)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID,  Names.signupButton))
    login.click()
    sleep(5)
    # Fill in the email field and submit
    input_field = driver.find_element(By.ID, Names.sigupEmailSpace)
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    # Fill in the form with incorrect user details
    fill(driver, email, first_name, last_name, password)
    # Click the confirm button
    input_field = driver.find_element(By.ID, Names.ConfirmButtonXPATH)
    input_field.click()
    sleep(5)
    # Agree to the terms and conditions
    # driver.find_element(By.XPATH, AgreeButtonXPATH).click()
    # sleep(20)
    # Check if the username is present in the page source
    assert "Please enter a valid email" in driver.page_source
    # Close the driver
    driver.close()

def testSignUpWrongEmailDomian():
    # Initialize the web driver
    driver = WebsiteDriverInit.init()
    # Generate a random username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add a domain name to the email
    email = username + '@karam'
    # Navigate to the website and click the signup button
    driver.get(mainURL)
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID,  Names.signupButton))
    login.click()
    sleep(5)
    # Fill in the email field with incorrect email
    input_field = driver.find_element(By.ID, Names.sigupEmailSpace)
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    # Check if the error message is
    assert "Please enter a valid email address" in driver.page_source
    driver.close()

def testSignUpWithoutPassword():
    # Initialize the website driver
    driver = WebsiteDriverInit.init()
    # Generate first and last name
    first_name,last_name=FirstLastName()
    # Create a random email and username
    email,username=createEmail()
    # Set an empty password
    password=""
    # Open the website
    driver.get(mainURL)
    # Find and click the sign up button
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID,  Names.signupButton))
    login.click()
    sleep(5)
    # Enter the email
    input_field=driver.find_element(By.ID,Names.sigupEmailSpace)
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(5)
    # Fill the sign up form
    fill(driver,email,first_name,last_name,password)
    input_field=driver.find_element(By.ID ,Names.ConfirmButtonXPATH)
    input_field.click()
    sleep(5)
    # Check for the expected error message
    assert "Please enter a valid password" in driver.page_source
    # Close the driver
    driver.close()   

def testSignUpEmptyEmail():
    # Initialize the website driver
    driver = WebsiteDriverInit.init()
    # Open the website
    driver.get(mainURL)
    # Find and click the sign up button
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID,  Names.signupButton))
    login.click()
    sleep(5)
    # Press enter without entering the email
    input_field=driver.find_element(By.ID,Names.sigupEmailSpace)
    input_field.send_keys(Keys.RETURN)
    sleep(3)
    # Check for the expected error message
    assert "Please enter a valid email address" in driver.page_source
    # Close the driver
    driver.close()

def testSignUpAssociatedEmail():
        # Initialize the website driver
    driver = WebsiteDriverInit.init()
    # Open the website
    driver.get(mainURL)
    # Set an email that already has an account
    usernameT=" miraaayman7770@gmail.com"
    # Find and click the sign up button
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID,  Names.signupButton))
    login.click()
    sleep(5)
    # Enter the existing email
    input_field=driver.find_element(By.ID,Names.sigupEmailSpace)
    input_field.send_keys(usernameT)
    input_field.send_keys(Keys.RETURN)
    sleep(3)
    # Check for the expected error message
    assert "Please enter a valid email" in driver.page_source
    # Close the driver
    driver.close()

# Define a test case that checks if different emails cause an error during sign-up.
def testSignUpDiffrentEmails():
    # Initialize the website driver.
    driver = WebsiteDriverInit.init()
    # Generate first and last names for the sign-up form.
    first_name,last_name=FirstLastName()
    # Generate an email address, username, and password for the sign-up form.
    email,username=createEmail()
    password=ceatePasword()
    # Navigate to the main URL for the website.
    driver.get(mainURL)
    # Find and click on the sign-up button using a wait condition and an XPATH.
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID,  Names.signupButton))
    login.click()
    # Wait for 5 seconds for the sign-up form to load.
    sleep(5)
    # Find the email input field and enter the generated email address.
    input_field=driver.find_element(By.ID,Names.sigupEmailSpace)
    input_field.send_keys(email)
    # Send the "Enter" key to submit the email address.
    input_field.send_keys(Keys.RETURN)
    # Wait for 5 seconds for the page to load.
    sleep(5)
    # Generate a new email address, username, first name, last name, and password for the sign-up form.
    email,username=createEmail()
    fill(driver,email,first_name,last_name,password)
    # Find and click on the confirm button using an XPATH.
    input_field=driver.find_element(By.ID ,Names.ConfirmButtonXPATH)
    input_field.click()
    # Wait for 5 seconds for the page to load.
    sleep(5)
    # Assert that the string "Email address doesn't match. Please try again" is in the page source.
    assert "Email address doesn't match. Please try again." in driver.page_source
    # Close the driver.
    driver.close()

# Define a test case that checks if not providing a first name causes an error during sign-up.
def testSignUpWithoutFirstName():
    # Initialize the website driver.
    driver = WebsiteDriverInit.init()
    # Generate a last name, email address, username, and password for the sign-up form.
    first_name,last_name=FirstLastName()
    first_name=""
    email,username=createEmail()
    password=ceatePasword()
    # Navigate to the main URL for the website.
    driver.get(mainURL)
    # Find and click on the sign-up button using a wait condition and an XPATH.
    login = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID,  Names.signupButton))
    login.click()
    # Wait for 5 seconds for the sign-up form to load.
    sleep(5)
    # Find the email input field and enter the generated email address.
    input_field=driver.find_element(By.ID,Names.sigupEmailSpace)
    input_field.send_keys(email)
    # Send the "Enter" key to submit the email address.
    input_field.send_keys(Keys.RETURN)
    # Wait for 5 seconds for the page to load.
    sleep(5)
    # Fill out the sign-up form with the generated email address, last name, password, and empty first name.
    fill(driver,email,first_name,last_name,password)
    # Find and click on the confirm button using an XPATH.
    input_field=driver.find_element(By.ID ,Names.ConfirmButtonXPATH)
    input_field.click()
    # Wait for 5 seconds for the page to load.
    sleep(5)
    # Assert that the string "First name is required" is in the page source.
    assert "First name is required"
