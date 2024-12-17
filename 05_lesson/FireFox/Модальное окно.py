from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Настройка драйвера
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Нажать на кнопку Close в модальном окне
time.sleep(2)  # Ждем, чтобы модальное окно успело загрузиться
driver.find_element(By.CSS_SELECTOR, ".modal-footer > a").click()

driver.quit()