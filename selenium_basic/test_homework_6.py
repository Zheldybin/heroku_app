import pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@pytest.mark.parametrize(
    "tr,td,expected",
    [
        (1, 1, "Smith"),
        (2, 3, "fbach@yahoo.com"),
        (4, 2, "Tim"),
        (3, 4, "$100.00")
    ]
)
def test_tables(browser, tr, td, expected):
    browser.get("https://the-internet.herokuapp.com/tables")
    element = browser.find_element(By.XPATH, f'//table[1]//tbody/tr[{tr}]/td[{td}]')
    assert element.text.strip() == f"{expected}", "В этой ячейке таблицы другой текст"
