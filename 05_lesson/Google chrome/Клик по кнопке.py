from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Настройка драйвера
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Кликнуть 5 раз на кнопку "Add Element"
for _ in range(5):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

# Собрать список кнопок "Delete"
delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
print("Количество кнопок Delete:", len(delete_buttons))
