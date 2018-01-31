from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_selenium():
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True
    profile.set_preference('dom.webnotifications.enabled', False)

    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
