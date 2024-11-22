from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Class for Testing Login
class LoginTest:
    # Test Data for Positive Login Test
    username = "student"
    password = "Password123"

    # Test data for negative login test 
    username1 = "incorrectUser"
    password1 = "incorrectPassword "

    # Test Locators 
    username_locator = '//*[@id="username"]' # Locates username
    password_locator = '//*[@id="password"]' # Locates password
    submit_button_locator = '//*[@id="submit"]' # Locates submit button
    logout_button_locator ='//*[@id="loop-container"]/div/article/div[2]/div/div/div/a' # Locates logout button
    login_error_text_locator = '//*[@id="error"]' # Locates error message abot invalid user and invalid password
    
# Define the class constructor (__init__) method
    def __init__(self, url):
        # Store the given URL as an instance variable
        self.url = url
        
        # Initialize a Chrome WebDriver instance to interact with web pages
        self.driver = webdriver.Chrome()

    # Method for Login
    def login(self):
        self.driver.maximize_window() # Maximize window
        self.driver.get(self.url) # Go to webpage
        sleep(5)
        
        # enter user name
        self.driver.find_element(by=By.XPATH, value=self.username_locator).send_keys(self.username)
        sleep(2)

        # Enter password
        self.driver.find_element(by=By.XPATH, value=self.password_locator).send_keys(self.password)
        sleep(2)

        # Click on submit
        self.driver.find_element(by=By.XPATH, value=self.submit_button_locator).click()
        sleep(5)

        # Click on logout
        self.driver.find_element(by=By.XPATH, value=self.logout_button_locator).click()
        sleep(2)

        if self.driver.current_url =="https://practicetestautomation.com/practice-test-login/":
            print("SUCCESS : TEST CASE PASSED")
            return True
        else:
            return False

    # Method for login with wrong username
    def NegativeUsername(self):
        
        # enter user name
        self.driver.find_element(by=By.XPATH, value=self.username_locator).send_keys(self.username1)
        sleep(2)

        # Enter password
        self.driver.find_element(by=By.XPATH, value=self.password_locator).send_keys(self.password)
        sleep(2)

        # Click on submit
        self.driver.find_element(by=By.XPATH, value=self.submit_button_locator).click()
        sleep(3)

        # to get the error text for assertion

        invalid_username_text = self.driver.find_element(by=By.XPATH, value=self.login_error_text_locator).text
        if invalid_username_text =="Your username is invalid!":
            print("Your username is invalid!")
            return True
        else:
            print("Failed, Unexpected Error!")
            return False 
  
    # Method for login with wrong password
    def NegativePassword(self):
        
        # enter user name
        self.driver.find_element(by=By.XPATH, value=self.username_locator).send_keys(self.username)
        sleep(2)

        # Enter password
        self.driver.find_element(by=By.XPATH, value=self.password_locator).send_keys(self.password1)
        sleep(2)

        # Click on submit
        self.driver.find_element(by=By.XPATH, value=self.submit_button_locator).click()
        sleep(3)

        invalid_password_text = self.driver.find_element(by=By.XPATH, value=self.login_error_text_locator).text
        if invalid_password_text =="Your password is invalid!":
            print("Your password is invalid!")
            return True
        else:
            print("Failed, Unexpected Error!")
            return False 

    # Shutdown Method
    def shutdown(self):
        self.driver.quit()
        return None