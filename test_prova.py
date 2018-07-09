from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_sel1():

    capabilities = DesiredCapabilities.CHROME
    driver = webdriver.Remote(command_executor='http://selenium:4444/wd/hub',desired_capabilities=capabilities)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    driver.quit()
    
