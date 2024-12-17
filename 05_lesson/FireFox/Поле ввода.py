from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройка драйвера
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

# Ввести текст 1000
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_field.send_keys("1000")

# Очистить поле
input_field.clear()

# Ввести текст 999
input_field.send_keys("999")

driver.quit()