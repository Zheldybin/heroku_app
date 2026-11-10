import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.regression
def test_inputs(browser):
    browser.get("https://the-internet.herokuapp.com/inputs")
    input = browser.find_element(By.TAG_NAME, "input")
    input.clear()
    input.send_keys(Keys.ARROW_DOWN)
    assert input.get_attribute("value") == "-1"
    input.clear()
    input.send_keys(Keys.ARROW_UP)
    assert input.get_attribute("value") == "1"
    input.clear()
    input.send_keys("abc")
    assert input.get_attribute("value") == "", "буквы ввелить в инпут типа number"
