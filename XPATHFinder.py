from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip

def get_element_xpath(url, element_id):
    # Create a new instance of the Edge driver
    path = r"C:\Users\youss\Desktop\SWE\msedgedriver.exe"
    driver = webdriver.Edge(path) 
    
    # Navigate to the provided URL
    driver.get(url)
    
    # Find the element by its ID
    element = driver.find_element(By.ID, element_id)
    
    # Get the XPath of the element
    xpath = get_element_xpath_helper(driver, element)

    # Close the browser
    driver.quit()
    
    # Return the XPath
    return xpath
    
def get_element_xpath_helper(driver, element):
    # Get the parent element of the provided element
    parent = element.find_element(By.XPATH, "..")
    
    # Get all child elements of the parent element with the same tag name
    siblings = parent.find_elements(By.TAG_NAME, element.tag_name)
    
    # If there is only one child element with the same tag name, return the XPath of the element
    if len(siblings) == 1:
        return f"//{element.tag_name}[@id='{element.get_attribute('id')}']"
    
    # Otherwise, build the XPath based on the index of the element among its siblings
    else:
        index = siblings.index(element) + 1
        return f"//{element.tag_name}[@id='{element.get_attribute('id')}'][{index}]"

# Example usage
url = "https://www.eventbrite.com/"
element_id = input("Enter the ID of the element: ")
xpath = get_element_xpath(url, element_id)

print(f"The XPath of the element with ID '{element_id}' is: {xpath}")
pyperclip.copy(xpath)
