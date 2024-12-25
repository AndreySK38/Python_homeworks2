from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

# Переход на страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ожидаем загрузки всех изображений
images = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
)

# Получаем значение атрибута src у 3-й картинки
if len(images) >= 3:
    print(images[2].get_attribute("src"))

driver.quit()

