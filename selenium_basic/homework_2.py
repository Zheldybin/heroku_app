from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/checkboxes")
checkboxs = driver.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
assert checkboxs[0].is_selected() == False, "Первый чекбокс уже отмечен"
checkboxs[0].click()
assert checkboxs[0].is_selected() == True, "Первый чекбокс еще не отмечен"
assert checkboxs[1].is_selected() == True, "Второй чекбокс еще не отмечен"
checkboxs[1].click()
assert checkboxs[1].is_selected() == False, "Второй чекбокс уже отмечен"
driver.quit()
