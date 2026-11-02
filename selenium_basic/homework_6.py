from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/tables")

element_1 = driver.find_element(By.XPATH, "//table[1]//tbody/tr[1]/td[1]")
assert element_1.text.strip() == "Smith", "В этой ячейке таблицы другой текст"
element_2 = driver.find_element(By.XPATH, "//table[1]//tbody/tr[2]/td[3]")
assert element_2.text.strip() == "fbach@yahoo.com", "В этой ячейке таблицы другой текст"
element_3 = driver.find_element(By.XPATH, "//table[1]//tbody/tr[4]/td[2]")
assert element_3.text.strip() == "Tim", "В этой ячейке таблицы другой текст"
element_4 = driver.find_element(By.XPATH, "//table[1]//tbody/tr[3]/td[4]")
assert element_4.text.strip() == "$100.00", "В этой ячейке таблицы другой текст"
driver.quit()