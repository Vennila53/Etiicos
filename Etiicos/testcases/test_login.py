import time
import pytest
from selenium import webdriver
from pageobjects.Loginpage import Loginpage
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen
#his is a test class containing test methods related to login functionality.
class Test_001_Login:
    read_config = ReadConfig()
    baseURL = read_config.getApplicationURL()
    username = read_config.getuseremail()
    password = read_config.getpassword()
    logger = LogGen.loggen()

# It ensures that each test starts with a fresh browser instance and closes
    # it after the test is finished.

    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = webdriver.Chrome()
        yield self.driver
        self.driver.quit()
#self log info used to provide information about the test execution process and any errors encountered
#duringtest.

    def test_homepagetitle(self, setup):
        self.logger.info("************Test_001_Login************")
        self.logger.info("************Verify Home Page Title************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Etiicos Login":
            assert True
            self.driver.close()
            self.logger.info("******Home page title is passed********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homepagetitle.png")
            self.driver.close()
            self.logger.error("************Home page title is failed************")
            assert False
#verify the expected outcomes of the page. if the assertions fails the test case failed and error get loggeda
    def test_login(self, setup):
        self.logger.info("************Verifying Login Test************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        act_title2 = self.driver.title
        print("Actual title2:", act_title2)
        time.sleep(5)
        if act_title2.strip() == "Etiicos - Hospitals":
            assert True
            self.logger.info("******Login Test is passed********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.logger.error("******Login Test is failed********")
            self.driver.close()
            assert False
# pytest -v -s testcases/test_login.py --browser chrome
#pytest -s -v --html=reports/report.html testcases/test_login.py -k "test_login" --browser chrome
