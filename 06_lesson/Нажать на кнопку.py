from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажимаем на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

# Ожидаем появления зеленой плашки и выводим текст
green_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "ajax-content"))
)
print(green_box.text)

driver.quit()
