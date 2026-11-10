import pytest
from selenium.webdriver.common.by import By


@pytest.mark.regression
def test_typos(browser):
    count = 0
    max_count = 50
    corrected_text = "Sometimes you'll see a typo, other times you won't."
    browser.get("https://the-internet.herokuapp.com/typos")

    while count < max_count:
        paragraph = browser.find_element(By.XPATH, "//p[contains(text(), 'Sometimes you')]")
        actual = paragraph.text.strip()
        if actual != corrected_text:
            print(f"Опечатка найдена с попытки {count}: {actual}")
            break
        browser.refresh()
        count += 1

    assert count < max_count, f"Опечатка не найдена за {max_count} попыток"
