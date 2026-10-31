from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# allCharsAndSymbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ!@#$%^&*()_+-=[]{}|;':\",./<>?\\`~№"

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/inputs")
input = driver.find_element(By.TAG_NAME, "input")
input.clear()
input.send_keys(Keys.ARROW_DOWN)
assert input.get_attribute("value") == "-1"
input.clear()
input.send_keys(Keys.ARROW_UP)
assert input.get_attribute("value") == "1"
input.clear()
input.send_keys("abc")
assert input.get_attribute("value") == "", "буквы ввелить в инпут типа number"
driver.quit()

# через цикл не получилось прогнать все буквы и символы но визуально видно что вводится e, E, -, +
#for char in allCharsAndSymbols:
#    input.clear()
#    input.send_keys(char)
#    actual_value = input.get_property("value")
#    if actual_value == char:
#        print(f"символ {char} ввелся в инпут")