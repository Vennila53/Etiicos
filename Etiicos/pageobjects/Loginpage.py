from selenium.webdriver.common.by import By

class Loginpage:
    textbox_username_id = "txtUser"
    textbox_password_id = "txtPwd"
    button_login_xpath = "//div[@class='ripple-ripple js-ripple']"
    link_logout_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver
#def-This keyword indicates the start of a function definition.
#init-This is the speciL method name for the constructor method.
# this line is used to initialize and store a driver object within instances of the class
#Finds the  input element on the page using its ID (txtUser)and sends the provided username parameter to it.
    def setUserName(self, username):
        try:
            username_element = self.driver.find_element(By.ID, self.textbox_username_id)
            username_element.send_keys(username)
        except Exception as e:
            print(f"Error setting username: {e}")

    def setPassword(self, password):
        try:
            password_element = self.driver.find_element(By.ID, self.textbox_password_id)
            password_element.send_keys(password)
        except Exception as e:
            print(f"Error setting password: {e}")

    def clickLogin(self):
        try:
            login_button = self.driver.find_element(By.XPATH, self.button_login_xpath)
            login_button.click()
        except Exception as e:
            print(f"Error clicking login button: {e}")

    # def clickLogout(self):
    #     try:
    #         logout_link = self.driver.find_element(By.LINK_TEXT, self.link_logout_link_text)
    #         logout_link.click()
    #     except Exception as e:
    #         print(f"Error clicking logout link: {e}")
