from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def test_selenium():
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True
    profile.set_preference('dom.webnotifications.enabled', False)

    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


def test_remote():
    # profile = webdriver.FirefoxProfile()
    # profile.accept_untrusted_certs = True
    # profile.set_preference('dom.webnotifications.enabled', False)

    capabilities = DesiredCapabilities.CHROME
    capabilities['marionette'] = False
    #capabilities['platform'] = "WINDOWS"
    #capabilities['version'] = "7"

    driver = webdriver.Remote(command_executor='http://172.30.21.81:4444/wd/hub',desired_capabilities={acceptSslCerts=true, marionette=false, browserName=chrome, javascriptEnabled=true, chromeOptions={args=[disable-infobars]}, platformName=ANY, version=, platform=ANY})
    driver.get("http://www.python.org")
    assert "Python" in driver.title

    assert True
    driver.close()
