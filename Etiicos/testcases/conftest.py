import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser.......")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser.......")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#################Pytest HTML Report##################

# It is a hook for adding environment info in HTML report
def pytest_configure(config):
    if not hasattr(config, '_metadata'):
        config._metadata = {}
    config._metadata['Project Name'] = "Etiicos"
    config._metadata['Module Name'] = "Customers"
    config._metadata['Tester'] = "Vennila"

# It is a hook for deleting/modifying environment info in HTML report
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)