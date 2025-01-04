from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройка драйвера
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

# Ввести данные
driver.find_element(By.NAME, "username").send_keys("tomsmith")
driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")

# Нажать кнопку Login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.quit()