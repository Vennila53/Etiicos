from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def select_dropdown_by_visible_text(self, locator, text):
        dropdown = Select(self.driver.find_element(*locator))
        dropdown.select_by_visible_text(text)

    def accept_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def switch_to_frame(self, locator):
        frame = self.driver.find_element(*locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def check_checkbox(self, locator):
        checkbox = self.driver.find_element(*locator)
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_checkbox(self, locator):
        checkbox = self.driver.find_element(*locator)
        if checkbox.is_selected():
            checkbox.click()

    def select_radio_button(self, locator):
        radio_button = self.driver.find_element(*locator)
        if not radio_button.is_selected():
            radio_button.click()
