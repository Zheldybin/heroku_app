import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.regression
def test_dropdown(browser):
    browser.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = browser.find_element(By.ID, "dropdown")
    select = Select(dropdown)
    select_options = select.options
    assert len(select_options) > 0, "Опции нет"
    select.select_by_index(1)
    assert select.first_selected_option.text.strip() == "Option 1", "Выбрана не первая опция"
    select.select_by_index(2)
    assert select.first_selected_option.text.strip() == "Option 2", "Выбрана не вторая опция"
