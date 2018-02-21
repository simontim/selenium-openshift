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

    capabilities = DesiredCapabilities.FIREFOX  # .copy()
    capabilities['marionette'] = False
    #capabilities['platform'] = "WINDOWS"
    #capabilities['version'] = "7"

    driver = webdriver.Remote(
            #browser_profile=profile,
            #command_executor='http://10.129.2.24:4444/wd/hub',
         #command_executor='http://10.130.3.47:4444/wd/hub',
            #command_executor='http://selenium-hub:4444/wd/hub',
             #command_executor='http://127.0.0.1:4444/wd/hub',
        command_executor='http://156.54.176.85:4444/wd/hub',
        
        #command_executor='http://selenium-display:4444/wd/hub',
          #command_executor='http://stand-fire:4444/wd/hub',
                              desired_capabilities=capabilities)

    #        command_executor='http://156.54.176.85:4444/wd/hub'

    driver.get("http://www.python.org")
    assert "Python" in driver.title

    assert True
    driver.close()
