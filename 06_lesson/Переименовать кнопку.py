from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/textinput")

# Указываем текст в поле ввода
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
input_field.send_keys("SkyPro")

# Нажимаем на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

# Ожидаем изменения текста кнопки и выводим его
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".btn.btn-primary"), "SkyPro")
)
print(button.text)

driver.quit()
