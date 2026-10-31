from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

count = 0
max_count = 50
corrected_text = "Sometimes you'll see a typo, other times you won't."

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/typos")

while count < max_count:
    paragraph = driver.find_element(By.XPATH, "//p[contains(text(), 'Sometimes you')]")
    actual = paragraph.text.strip()
    if actual != corrected_text:
        print(f"Опечатка найдена с попытки {count}: {actual}")
        break
    driver.refresh()
    count += 1

assert count < max_count, f"Опечатка не найдена за {max_count} попыток"
driver.quit()