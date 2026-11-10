import pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_remove_element(browser):
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_element = browser.find_element(By.XPATH, "//button[text()='Add Element']")
    add_element.click()
    add_element.click()
    elements = browser.find_elements(By.XPATH, "//button[text()='Delete']")
    assert len(elements) == 2, "Количество элементов не равно двум"
    elements[0].click()
    elements = browser.find_elements(By.XPATH, "//button[text()='Delete']")
    assert len(elements) == 1, "Количество элементов не равно 1"
