from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройка драйвера
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

# Кликнуть на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

driver.quit()