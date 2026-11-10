import pytest
from selenium.webdriver.common.by import By


@pytest.mark.regression
def test_checkboxes(browser):
    browser.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxs = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    assert checkboxs[0].is_selected() == False, "Первый чекбокс уже отмечен"
    checkboxs[0].click()
    assert checkboxs[0].is_selected() == True, "Первый чекбокс еще не отмечен"
    assert checkboxs[1].is_selected() == True, "Второй чекбокс еще не отмечен"
    checkboxs[1].click()
    assert checkboxs[1].is_selected() == False, "Второй чекбокс уже отмечен"
