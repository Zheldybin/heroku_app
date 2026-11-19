import pytest
from selenium.webdriver.common.by import By


@pytest.mark.regression
def test_typos(browser):
    corrected_text_one = "Sometimes you'll see a typo, other times you won't."
    corrected_text_two = "Sometimes you'll see a typo, other times you won,t."
    browser.get("https://the-internet.herokuapp.com/typos")
    paragraph = browser.find_element(By.XPATH, "//p[contains(text(), 'Sometimes you')]")
    actual = paragraph.text.strip()
    assert actual == corrected_text_one or actual == corrected_text_two

